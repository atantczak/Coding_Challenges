import numpy as np
import math

'''
Write a piece of code to find the most frequently occurring element in an array.
'''


def freq_array(arr1):
    el_array = {}
    for i in arr1:
        el_array["{}".format(i)] = 0

    for i in arr1:
        el_array["{}".format(i)]+=1

    max_entry = max(el_array)

    return max_entry


print(freq_array([3, 4, 5, 10, 5]))


