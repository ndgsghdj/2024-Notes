correct = False
while not correct:
    arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

    while True:
        try:
            locker = int(input("Please enter the locker you would like to open: "))
            assert 1 <= locker <= 10
            break
        except:
            print("Locker number must be between 1 and 10.")

    while True:
        try:
            pin = input("Please enter the PIN for the locker: ")
            assert len(pin) == 4
            break
        except:
            print("PIN must be 4 digits.")
        
    pin[::-1]
    pin_int = 0

    for i in range(len(pin)):
        pin_int += pin[i] * 10**i

    pin = pin_int

    if pin == arraypins[locker - 1]:

        print ("The locker is open")
        correct = True

    else:

        print ("Incorrect PIN for that locker")
