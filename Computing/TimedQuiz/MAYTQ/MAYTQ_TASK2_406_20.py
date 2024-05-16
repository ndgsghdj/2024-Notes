# MAYTQ_TASK2

# 1. Write a function is_repetitive()

def is_repetitive(message):

    string = message

    if len(message) <= 1:
        return False

    if len(string) % 2 != 0:
        string = ''.join([string[0:len(string)//2], string[len(string)//2+1:]])
        print(f"New String: {string}")

    for c in string:
        if not c.isalnum():
            new_string = [c for c in string]
            new_string.pop(string.index(c))

            string = ''.join(new_string)
        string = ''.join([c.lower() for c in string])

    if string[0:len(string)//2] == string[len(string)//2:]:
        return True

    return False

# 2. The following code is to read data from the given text file
#    You may uncomment and use the given code or write one yourself

with open("Task2B_data.txt", "r") as fin:

    #Read in the 1st line of the file
    n = int(fin.readline())

    #For the next n lines, read one line at a time.
    for i in range(n):
        s = fin.readline()
        print(s, "Has repetitive pattern: ", is_repetitive(s))
