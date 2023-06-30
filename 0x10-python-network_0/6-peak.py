#!/usr/bin/python3

""" this script contains a function that finds the peak 
    in an unsorted list
    """

def find_peak(list_of_integers):
    """
    this function returns the peak value in an unsorted list
    """

    set_num = set(list_of_integers)

    if len(set_num) == 0:
        return None
    if len(set_num) == 1:
        return list_of_integers[0]
    if max(list_of_integers) == list_of_integers[-1]\
            or max(list_of_integers) == list_of_integers[0]:
                return max(list_of_integers)
    for num in set_num:
        ind = [i for i, n in enumerate(list_of_integers) if n == num]
        for i in ind:
            if i == 0 and list_of_integers[0] != max(list_of_integers):
                if list_of_integers[i] > list_of_integers[i + 1]:
                    peak = list_of_integers[i]
                    break
            else:
                if list_of_integers[i] > list_of_integers[i - 1]\
                        and list_of_integers[i] > list_of_integers[i + 1]:
                            peak = list_of_integers[i]
                            break
    return peak
