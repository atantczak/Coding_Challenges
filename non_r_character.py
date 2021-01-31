import numpy as np
import math

'''
Given a string, find the first non-repeating character in it. For example, if the input string is 
“GeeksforGeeks”, then the output should be ‘f’ and if the input string is “GeeksQuiz”, then the output should be ‘G’.
'''


def non_repeat(inp_str):
    count = {}
    for element in str(inp_str):
        count["{}".format(element)] = 0

    for element in str(inp_str):
        count["{}".format(element)]+=1

    for i in count:
        j = count[i]
        if j == 1:
            print(i)
            return
        else:
            continue

    return


non_repeat('GeeksQuiz')


