import os
import json
from time import sleep
import subprocess
import requests


def main():
    try:
        HOST = "pc16.leela"
        PORT = 5000
        MESSAGE = 'Password Not Found'
        FOUND_PASS = 'false'
        TRUECRACK_PATH = '/netexport/tmp/truecrack-3/bin/truecrack'
        HEADER_PATH = '/netexport/tmp/Header'
        DICT_PATH = '/netexport/tmp/dictionary.txt'
        REFETCH_PERIOD = 2
        WORD_SIZE = 50

        lFileSize = os.stat(DICT_PATH).st_size

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
                sleep(REFETCH_PERIOD)

            lRangeId = lRange['job'][0]
            lNumRanges = lRange['job'][1]

            # Calculate the number of lines to process
            #lines = lRange['lines'] * (lRangeId + 1)

            print "Execute the following job: " + str(lRangeId) + \
                " of " + lNumRanges

            lFH = open(DICT_PATH, "rb")
            lOffsetBegin = float(lRangeId) / lNumRanges * lFileSize - WORD_SIZE
            lOffsetEnd = float(lRangeId + 1) / lNumRanges * lFileSize
            if lRangeId is not 0:
                lFH.seek(
                    lOffsetBegin,
                    os.SEEK_SET
                )

            # Start truecrack
#            pass_check = subprocess.check_output(
#                [TRUECRACK_PATH, '-t', HEADER_PATH, '-w', DICT_PATH]
#            )

            lTrueCrack = subprocess.Popen(
                [TRUECRACK_PATH, "-t", HEADER_PATH, "-w", "-"],
                bufsize=512,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE
            )

            # interact with truecrack
            while lFH.tell() < lOffsetEnd:
                # read password (line) from file
                lPass = lFH.readline()

                # forward password to process
                lTrueCrack.stdin.write(lPass)
                # sync/flush
                lTrueCrack.stdin.flush()

                print("==== START TrueCrack output ====")

                while True:
                    lLine = lTrueCrack.stdout.readline()
                    if lLine == '':
                        break
                    print(lLine)

                # get output and parse
                # if password has been found => break
#                if 'Found password' in pass_check:
#                    MESSAGE = pass_check.split()[9]
#                    FOUND_PASS = 'true'
#                    break
                print("==== END TrueCrack output ====")

            # notify server

            # Print truecrack's output
            #print pass_check

            # Determine if the password has been found

            lResponse = requests.get(
                "http://" + HOST + ":" + str(PORT) + "/report?" +
                "success=" + FOUND_PASS +
                "&rangeId=" + str(lRangeId) +
                "&message=" + MESSAGE
            )

    except Exception, pExc:
        print "Error. " + str(pExc)


if __name__ == '__main__':
    main()
