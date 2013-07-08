import sys
import json

import requests


def main():
    try:
        HOST = "localhost"
        PORT = 5000

        lResponse = requests.get(
            "http://" + HOST + ":" + str(PORT) + "/fetch"
        )
        lRange = json.loads(lResponse.text)
        if 'job' in lRange:
            print "Execute the following job: " + str(lRange['job'])
    except ValueError:
        print "Error. "

if __name__ == '__main__':
    main()
