import numpy as np
import math
import time

'''
Write a function to determine if a number is prime.
'''


def prime(x):

    d = 0
    for i in range(1, x+1):
        if x % i == 0:
            d+=1

    if d == 2:
        print("{} is a prime number.".format(x))
    else:
        print("{} is not a prime number.".format(x))
    return


prime(7229)


