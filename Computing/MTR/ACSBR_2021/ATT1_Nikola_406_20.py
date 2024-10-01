days = ["Mon", "Tues", "Wed", "Thu", "Fri"]
attendance = []

for i in range(5):
    while True:
        try:
            attendance_day = input("Enter attendance for {}: ".format(days[i]))
            for c in attendance_day:
                assert c in "pea ".upper()
            assert len(attendance_day.split(" ")) == 5
            break
        except:
            print("Invalid. Try again.")
    
    attendance_count = attendance_day.count("P")
    attendance.append(attendance_count)

for i in range(5):
    print("{}    {} student(s) are present".format(days[i], attendance[i]))

attendance_rate = sum(attendance)/(5 * 5) * 100
print("Weekly attendance rate = {}%".format(round(attendance_rate, 1)))
