# This is NUMBERS.py
# Have fun!
# Please start coding...

while True:
    while True:
        try:
            A = input("Enter a three digit number: ")
            assert len(A) == 3
            assert A[0] != A[-1]
            break
        except:
            print("Number must be a three-digit number whose first and third digits are not the same.")

    B = int(A[::-1])
    A = int(A)

    if A > B:
        X = A - B
        print("{} - {} = {}".format(A, B, X))
    else:
        X = B - A
        print("{} - {} = {}".format(B, A, X))

    Y = int(str(X)[::-1])
    result = X + Y
    print("{} + {} = {}".format(X, Y, result))

    cont = input("Do you want to try again? [Y/N] ")
    if cont == "N":
        break
