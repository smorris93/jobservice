import sys
import json
from random import randint
from time import sleep

import requests


def main():
    try:
        HOST = "localhost"
        PORT = 5000
        MESSAGE = "asd-0fi83k"

        # job loop
        while True:
            lRange = {}
            # request loop
            while True:
                lResponse = requests.get(
                    "http://" + HOST + ":" + str(PORT) + "/fetch"
                )
                lRange = json.loads(lResponse.text)
                if 'job' in lRange:
                    break
                sleep(2)

            lRangeId = lRange['job'][0]

            print "Execute the following job: " + str(lRangeId)

            # randomly select if job has been processed successfully
            lResponse = requests.get(
                "http://" + HOST + ":" + str(PORT) + "/report?" +
                "success=" + ('true' if randint(1, 5) is 1 else 'false') +
                "&rangeId=" + str(lRangeId) +
                "&message=" + MESSAGE
            )

    except ValueError, pExc:
        print "Error. " + str(pExc)

if __name__ == '__main__':
    main()
