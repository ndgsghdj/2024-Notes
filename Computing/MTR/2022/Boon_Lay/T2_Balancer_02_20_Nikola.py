while True:
    strings = []
    print("Welcome to the string balancer")
    strings.append(input('string1: '))
    print("Length of st1: {}".format(strings[-1]))
    strings.append(input('string2: '))
    print("Length of st2: {}".format(strings[-1]))

    check = True
    for char in strings[1]:
        if char not in strings[0]:
            check = False

    if check == True:
        print("Strings are balanced")
    else:
        print("Strings are not balanced")

    if len(strings[0]) > len(strings[1]):
        print("String 1 is longer.")
    else:
        print("String 2 is longer.")

    if input("again (y/n): ").lower() != 'y':
        break

