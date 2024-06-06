from typing import Counter

students = int(input("How many students would you like to arrange consultations for?\n"))

consultation_days = []
for i in range (students):
    day = input("What is the student’s choice of consultation day? ")

    check = Counter(consultation_days)

    while check[day.upper()[:3]] + 1 > 5:

        day = input("The number of students for this particular day has already exceeded five. Please input another day:\n")

    day = day.upper()[:3]
    consultation_days.append(day)

consultation_days = Counter(consultation_days)

for day in consultation_days:
    print("Number of students for {}: {}".format(day, consultation_days[day]))
