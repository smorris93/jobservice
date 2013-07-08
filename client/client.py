import sys
import json

import requests


def main():
    try:
        lSuccess = sys.argv[1]
        lRangeId = sys.argv[2]

        lRequest = requests.get(
            "http://localhost:5000/report?success=" + lSuccess +
            "&rangeId=" + lRangeId + "&message=bla"
        )
        lRange = json.loads(lRequest.text)
        if 'job' in lRange:
            print "Execute the following job: " + lRange['job']
    except ValueError:
        print "Error. "
    except IndexError:
        print "Usage: " + sys.argv[0] + " <success> <rangeId>"

if __name__ == '__main__':
    main()
