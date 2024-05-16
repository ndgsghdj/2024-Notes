def signal_loss(dist):
    i = 0

    while (i+1)**2 <= dist:
        i += 1

    return i

# UI

while True:
    distance = int(input("Distance of receiver from transmitter: "))

    print("Steps of signal loss: {}".format(signal_loss(distance)))

    re_enter = input("Would you like to re-enter another value? Y/N\n")

    if re_enter.upper() == "Y":
        pass
    else:
        break


