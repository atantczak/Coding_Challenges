import numpy as np
import math

'''
You have a ladder of X steps. You can go up the ladder by taking either one or two steps each time. 
Write a function to determine how many potential different combinations of one or two steps you could take to the top 
of the ladder.
'''


def ladder(steps):

    choices = [1, 2]

    # steps = choices[0]*x + choices[1]*y

    n = 0
    for i in range(0, steps+1):
        x = (steps - choices[1]*i)/choices[0]
        if x.is_integer():
            if x < 0:
                continue
            else:
                print("You could take {} 1-step steps and {} 2-step steps".format(x, i))
                n+=1

    return n


print(ladder(57))


