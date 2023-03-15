#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0
    else:
        total = 0
        last = []
        for i in my_list:
            hold = 1
            for j in range(len(i)):
                hold *= i[j]
            total += hold
            last.append(i[-1])
        return (total/sum(last))
