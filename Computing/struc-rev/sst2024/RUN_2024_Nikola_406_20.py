students = ['Alice', 'Bob', 'Charlie', 'Daphne']
timings = [14.3, 10.9, 9.7, 16.1]
new_student = input("Please enter student's name: ")
students = students + [new_student]
while True:
    try:
        new_timing = float(input("Please enter student's timing: "))
        assert new_timing > 0
        break
    except:
        print("Timing must be a positive decimal number.")


timings = timings + [new_timing]
