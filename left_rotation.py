import numpy as np
import math

'''
A left rotation operation on an array shifts each of the array's elements  unit to the left.
'''


def left_rot(arr1, d):
    arr2 = arr1[d::] + arr1[0:d]

    return arr2


print(left_rot([1, 2, 3, 4, 7, 8, 4, 7, 4, 3, 8, 9, 5], 3))


