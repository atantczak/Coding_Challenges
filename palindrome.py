import numpy as np
import math

'''
Write a piece of code to determine whether a number is a palindrome.
'''


def palindrome(number):

    forward_num = number

    str_num = list(str(number))[::-1]

    reverse_num = float("".join(str_num))

    if forward_num == reverse_num:
        print("{} is a palindrome.".format(number))
    else:
        print("{} is not a palindrome.".format(number))

    return


palindrome(414)


