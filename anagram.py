import numpy as np
import math

'''
Write a piece of code to determine whether two words are anagrams.
'''


def anagrams(str1, str2):
    for letter in str1:
        if letter in str2:
            continue
        else:
            print("{} and {} are not anagrams".format(str1, str2))
            return

    print("{} and {} are anagrams".format(str1, str2))

    return


anagrams('adam', 'daam')


