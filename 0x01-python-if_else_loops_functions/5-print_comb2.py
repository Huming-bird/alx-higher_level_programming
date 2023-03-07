#!/usr/bin/python3
for number in range(100):
    if number != 99:
        print("{}, ".format('0' + str(number) if 
            \number < 10 else number), end='')
    else:
        print("{}".format(number))
