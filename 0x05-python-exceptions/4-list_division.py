#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    lis = list()
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError as e:
            print('division by 0')
            ans = 0
        except TypeError as er:
            print('wrong type')
            ans = 0
        except IndexError as err:
            print('out of range')
            ans = 0
        finally:
            lis.append(ans)
    return lis
