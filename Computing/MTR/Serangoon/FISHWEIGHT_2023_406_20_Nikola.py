numFish = int(input("Number of fish: "))
minWeight = 1.2
minLength = 30.0
for i in range(numFish):
    weight = float(input("Weight of fish: "))
    length = float(input("Length of fish: "))

    if weight >= minWeight and length >= minLength:
        print("This fish is heavy enough and long enough. Bag it for market.")
    elif not(weight >= minWeight and length >= minLength):
        print("This fish is not heavy and not long enough. Return to Original Section.")
    elif length < minLength:
        print("This fish is not long enough. Return to General Growth Section.")
    elif weight < minWeight:
        print("This fish is not heavy enough. Return to Weight Growth Section.")

