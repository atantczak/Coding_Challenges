import numpy as np
import math

'''
Add all digits together to produce super digit. If input is one digit long, super digit is itself.
'''


def super_digit(digit):

    str_digit = list(str(digit))

    if len(str_digit) == 1:
        n = int(digit)
        return n
    else:
        n = 0
        for i in str_digit:
            n+=float(i)
        n = int(n)

    return n


print(super_digit(2093485903485903485908))


