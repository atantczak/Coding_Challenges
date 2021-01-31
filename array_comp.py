import numpy as np
import math

'''
You have two arrays of integers. Write a piece of code to output an array that will only have elements found in one, but not both, arrays.
'''


def anagrams(arr1, arr2):
    arr3 = [x for x in arr1 if x not in arr2] + [x for x in arr2 if x not in arr1]
    print(arr3)

    return


anagrams([1, 2, 3, 4, 7, 8], [1, 2, 3, 4, 5, 11, 19])


