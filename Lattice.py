import numpy as np
import math

'''
Given a circle of radius r in 2-D with origin (0,0) as the center, the task is to find the total lattice points
on the circumference (w/ lattice points being coordinates made of integers in 2-D space).
'''


def lattice(r):
    if r <= 0:
        return r

    '''
    x^2 + y^2 = r^2
    '''

    pairs = []
    for i in range(-r, r+1):
        x = int(i)
        ys = np.sqrt(r*r - x*x)
        if ys.is_integer():
            pair = (x,ys)
            pairs.append(pair)
            if ys != 0:
                pair_n = (x,-ys)
            else:
                continue
            pairs.append(pair_n)

    print(pairs)
    print(len(pairs))

    return


lattice(10)

