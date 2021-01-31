import numpy as np
import math
import time

'''
How do you write a function that takes the square root of a number without using any built-in exponential function?
'''


def sqrt(x):
    # x = y*y

    for i in range(1, int(x/2)+1):
        if float(x)/float(i) == float(i):
            print("The square root is {}".format(i))
        else:
            continue

    return


def r_sqrt(x):
    num_array = []
    for i in range(1,x+1):
        if x % i == 0:
            num_array.append(i)
            sq = i*i
            if sq == x:
                num_array.append(i)

    print(num_array)

    dup = [x for x in num_array if num_array.count(x) > 1]
    if len(dup) > 1:
        print("Square root is {}".format(dup[1]))
    else:
        median = np.median(num_array)

        sq = median**2

        o_median = median
        l_median = 0

        while sq != x:
            sq = median**2

            if sq > x:
                o_median = median
                median = (median + l_median)/2.0
            if sq < x:
                l_median = median
                median = (median + o_median)/2.0

            est = str(sq)[0:3]
            if float(est) == float(x):
                print("The square root of {} is roughly {}".format(x, median))
                return

        print("The square root of {} is roughly {}".format(x, median))

    return


r_sqrt(1000)





