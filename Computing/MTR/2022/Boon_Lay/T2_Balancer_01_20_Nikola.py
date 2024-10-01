while True:
    print("Welcome to the string balancer")
    st1 = input('string1: ')
    print("Length of st1: {}".format(st1))
    st2 = input('string2: ')
    print("Length of st2: {}".format(st2))

    check = True
    for char in st2:
        if char not in st1:
            check = False

    if check == True:
        print("Strings are balanced")
    else:
        print("Strings are not balanced")

    if len(st1) > len(st2):
        print("String 1 is longer.")
    else:
        print("String 2 is longer.")

    if input("again (y/n): ").lower() != 'y':
        break

