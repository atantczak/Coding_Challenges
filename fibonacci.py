import numpy as np
import math
import time

'''
How do you write a function that takes the square root of a number without using any built-in exponential function?
'''


def fibb(x, tracker):

    if x == 0:
        tracker.append(x)
        x = x+1
    else:
        tracker.append(x)
        x = x + tracker[-2]

    print(x)
    time.sleep(1)

    return fibb(x, tracker)


#fibb(0, [])


def fibb_iteration():
    tracker = []

    x = 0
    tracker.append(x)
    run = True
    while run:
        if x == 0:
            x = x + 1
            tracker.append(x)
        else:
            x = x + tracker[-2]
            tracker.append(x)

        print(x)
        time.sleep(1)


fibb_iteration()


