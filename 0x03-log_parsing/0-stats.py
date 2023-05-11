#!/usr/bin/python3
"""
Log parsing
"""

import sys
stcd = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}
summ = 0


def prn_stats():
    """
    Function that print stats about log
    """
    global summ

    print('File size: {}'.format(summ))
    stcdor = sorted(stcd.keys())
    for each in stcdor:
        if stcd[each] > 0:
            print('{}: {}'.format(each, stcd[each]))


if __name__ == "__main__":
    cnt = 0
    try:
        """ Iter the standar input """
        for data in sys.stdin:
            try:
                fact = data.split(' ')
                """ If there is a status code """
                if fact[-2] in stcd:
                    stcd[fact[-2]] += 1
                """ If there is a lenght """
                summ += int(fact[-1])
            except:
                pass
            """ Printing control """
            cnt += 1
            if cnt == 10:
                prn_stats()
                cnt = 0
    except KeyboardInterrupt:
        prn_stats()
        raise
    else:
        prn_stats()
