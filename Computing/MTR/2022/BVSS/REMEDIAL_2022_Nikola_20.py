names = []
marks = []

while True:
    names.append(input("Student name: "))
    mark = ""

    while True:
        try:
            mark = float(input("Student's mark: "))
            assert 0 <= mark <= 100
            break
        except:
            print("Student's mark has to be between 0 and 100 inclusive.")

    marks.append(mark)

    more = input("Do you want to input another student's marks? [y/n] ")

    if more.lower() == "y":
        continue
    else:
        break

print("There are %d students" % len(names))    
average = sum(marks) / len(marks)
print("The average mark is %.1f" % average)

remedial = []
peer_tutors = 0

for i in range(len(marks)):
    if marks[i] < average:
        remedial.append(names[i])

if len(remedial) == 0: 
    print("There are no students for remedial")
else:
    peer_tutors = len(remedial) // 3
    if len(remedial) % 3 != 0:
        peer_tutors += 1

print("Number of peer tutors needed: %d" % peer_tutors)
