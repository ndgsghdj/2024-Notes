no_students = 5
days = ["Mon", "Tues", "Wed", "Thu", "Fri"]
attendance = []
students = [0] * no_students

for i in range(5):
    while True:
        try:
            attendance_day = input("Enter attendance for {}: ".format(days[i]))
            for c in attendance_day:
                assert c in "pea ".upper()
            assert len(attendance_day.split(" ")) == no_students
            break
        except:
            print("Invalid. Try again.")
    
    attendance_count = attendance_day.count("P")
    attendance.append(attendance_count)

    for i in range(no_students):
        if attendance_day.split()[i] == "P":
            students[i] += 1

for i in range(5):
    print("{}    {} student(s) are present".format(days[i], attendance[i]))

attendance_rate = sum(attendance)/(no_students * 5) * 100
print("Weekly attendance rate = {}%".format(round(attendance_rate, 1)))

for i in range(no_students):
    if students[i] >= 4:
        print("Student {} is present for {} days.".format(i, students[i]))
