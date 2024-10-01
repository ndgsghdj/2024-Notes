bags_rice = 10
upper_bound = 5.1
lower_bound = 4.9
count_underweight = 0
count_overweight = 0
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        count_overweight += 1
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")
        count_underweight += 1
    if lower_bound <= bag_weight <= upper_bound:
        print("The bag of rice is the correct weight.")

print("Number of underweight bags: {}".format(count_underweight))
print("Number of overweight bags: {}".format(count_overweight))
