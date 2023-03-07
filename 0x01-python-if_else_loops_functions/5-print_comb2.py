#!/usr/bin/python3
for a in range(100):
    if a != 99:
        print("{}, ".format('0' + str(a) if a < 10 else a), end='')
    else:
        print("{}".format(a))
