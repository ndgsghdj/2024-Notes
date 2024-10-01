students = ['Alice', 'Bob', 'Charlie', 'Daphne']
timings = [14.3, 10.9, 9.7, 16.1]
new_student = input("Please enter student's name: ")
if new_student not in students:
    students = students + [new_student]
while True:
    try:
        new_timing = float(input("Please enter student's timing: "))
        assert new_timing > 0
        break
    except:
        print("Timing must be a positive decimal number.")

for i in range(len(timings)):
    if students[i] == new_student:
        if new_timing >= timings[i]:
            print("New timing is slower than previous timing. Ignoring.")
        else:
            timings = timings + [new_timing]

