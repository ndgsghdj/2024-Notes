no_inputs = int(input("Number of inputs: "))
high = []
numbers = []

for count in range(no_inputs):
    while True:
        try:
            number = int(input('Enter a positive integer: '))
            assert 1 <= number
            break
        except:
            print("Number must be a positive integer")

    numbers.append(number)

    if number >= 1 and number <= 40:
        print(number, '- Low')
    elif number > 40 and number <= 70:
        print(number, '- Medium')
    elif number > 70 and number <= 100:
        print(number, '- High')
        high.append(number)

print("Average: {}".format(sum(numbers)/len(numbers)))
