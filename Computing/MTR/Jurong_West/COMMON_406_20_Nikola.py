#Task 2

multiples=[]
value = int(input("Enter an integer: "))
while not(value < 10 and value > 0):
    value = int(input("Values must be positive and less than 10. Please re-enter your integer: "))
for x in range(1,11):
    multiples = multiples + [value*x]

print("The multiples are", multiples)

multiples2 = []
value2 = int(input("Enter a second positive integer less than or equal to 10: "))

for x in range(1, 11):
    multiples2 = multiples2 + [value2*x]

print("The multiples are", multiples2)

print("Number of common multiples: {}".format(len(list(set.intersection(set(multiples), set(multiples2))))))
