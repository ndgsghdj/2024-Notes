sent = 0

rejected = 0

length_check = 15

width_check = 5

weight_check = 25

count = 0 #4

flag = True

while flag == True: #3

    package_length = int(input("Enter the length of the package: "))

    package_width = int(input("Enter the width of the package: "))

    package_weight = int(input("Enter the weight of the package: "))

    count = count + 1 #5

    if package_length > length_check or package_length < length_check:

        print("The package is rejected")

        rejected = rejected + 1

    elif package_width > width_check or package_width < width_check: #7

        print("The package is rejected")

        rejected = rejected + 1 #6

    elif package_weight > weight_check or package_weight < weight_check:

        print("The package is rejected")

        rejected = rejected + 1

    else:

        print("The package is the correct size and weight")

        sent = sent + 1 #8

    more_packages = input("Would you like to check another package, Y or N?: ") #9

    if more_packages == "N": #1

        flag = False

print("You checked " + str(count) + " packages.")

print(str(sent) + " " + "packages were sent and " + str(rejected) + " " + "packages were rejected") #2
