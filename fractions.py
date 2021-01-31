import numpy as np
import math

'''
Write a piece of code to combine fractions from two arrays into a single array.
'''


def anagrams(arr1, arr2):
    frac_array = []
    for i in range(0, len(arr1)):
        frac_array.append(float(arr1[i]/arr2[i]))

    return frac_array


print(anagrams([1, 2, 1, 5], [3, 4, 5, 10]))


