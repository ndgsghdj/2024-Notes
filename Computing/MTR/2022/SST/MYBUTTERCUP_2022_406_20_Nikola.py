print('Welcome to Buttercup Customised Bouquets!')
print('Enter up to three flowers to create your bouquet.')

flowers = ['red roses', 'pink roses', 'buttercups', "baby's breath", 'limonium'] #1
prices = [7, 9, 10, 3, 5]

counter = 0
cost = 0
while True: #2
    flower = input('Please choose a flower: ')
    flower = flower.lower() #3
    if flower not in flowers:
        print('Sorry, we do not have that flower. Please try again!')
        continue #10

    flower_index = flowers.index(flower)
    cost += prices[flower_index] #6
    counter += 1
    if counter == 3: #7
        cont = input('Please enter "N" to end, or any other key to continue: ').lower() #9
        if cont == 'n':
            cost += 5 #8
            break #4

if counter == 3:
    cost = float(round(0.9 * cost, 2)) #5

print('The cost of your bouquet is ${}.'.format(cost))

