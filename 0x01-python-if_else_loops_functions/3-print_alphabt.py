#!/usr/bin/python3
for number in range (97, 123):
    if (chr(number) == 'q' or chr(number) == 'e'):
        pass
    else:
        print("{}".format(chr(number)), end='')
