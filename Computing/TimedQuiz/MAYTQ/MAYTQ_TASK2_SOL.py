# MAYTQ_TASK2

# 1. Write a function is_repetitive()

import math

def is_repetitive(s):
    temp_string = ""

    for ch in s:
        if ch.alnum():
            temp_string += ch.lower()

    if len(temp_string) < 2:
        return False

    mid = len(temp_string)//2

    a = temp_string[:mid]
    b = temp_string[mid:]

    if len(temp_string) % 2 == 1:
        b = b[1:]

    mid2 = len(temp_string)/2
    a = temp_string[:math.floor(mid2)]
    b = temp_string[math.ceil(mid2):]

    return a == b

# 2. The following code is to read data from the given text file
#    You may uncomment and use the given code or write one yourself

with open("Task2B_data.txt", "r") as fin:

    #Read in the 1st line of the file
    n = int(fin.readline())

    #For the next n lines, read one line at a time.
    for i in range(n):
        s = fin.readline()
        s = s.rstrip()
        print("{}".format(s), end="")
        if is_repetitive(s):
            print(" is repetitive. ")
        else:
            print(" is not repetitive. ")
