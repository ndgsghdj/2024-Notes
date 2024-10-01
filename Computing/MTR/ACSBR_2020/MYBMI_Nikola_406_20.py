students = 15
upp_bound = 25
low_bound = 18.5

num_overweight = 0
num_underweight = 0

for count in range(students):
    weight = float(input('Enter weight of student in kg '))
    height = float(input('Enter height of student in cm '))
    bmi = weight/height**2 * 10000
    if bmi > upp_bound:
        print('Student is overweight')
        num_overweight += 1
    if bmi < low_bound:
        print('Student is underweight')
        num_underweight += 1
    if low_bound <= bmi <= upp_bound:
        print("Student's weight is normal")

print("Number of underweight students: {}".format(num_underweight))
print("Number of overweight students: {}".format(num_overweight))
    
