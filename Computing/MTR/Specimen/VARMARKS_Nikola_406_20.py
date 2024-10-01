test_highest = 0
test_lowest = 100
test_total = 0
student = int(input("Number of students: "))
for count in range(student):
    while True:
        try:
            test = int(input("Enter a mark for the test "))
            assert 0 <= test <= 100
            break
        except:
            print("Mark must be between 0 and 100. Please re-input.")
    if test_highest < test:
        test_highest = test
    elif test < test_lowest:
        test_lowest = test
    test_total = test_total + test
print("Highest mark for the test is ", test_highest)
print("Lowest mark for the test is ", test_lowest)
test_average = test_total/student
print("Average mark for the test is ", test_average)
