import numpy as np
import math

'''
A line with numbered individuals can be unorganized via a person cutting a maximum of two people. 
Figure out the minimum number of movements that occured to get line into current state. 
'''


def queue(line):
    m = 0
    for i in range(0, len(line)):
        if i == line[i]:
            continue
        else:
            diff = abs(int(i - line[i]))
            m+=diff

    m = float(m/2.0)
    return int(m)


llin = [1, 2, 3, 4, 5, 6]
line = [1, 4, 2, 6, 5, 3]
print(queue(line))

