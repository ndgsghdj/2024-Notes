no_data = int(input("Number of student data being entered: "))
distinctions = []
fails = []
scores = []
classes = "ABCDE"
levels = 4

for _ in range(no_data):
    name = input("Student name: ").upper()
    score = 0
    className = ""

    while True:
        try:
            className = input("Student's class: ")
            assert 1 <= int(className[0]) <= levels
            assert className[1] in classes
            break
        except:
            print("Class is invalid.")

    print("Class: {}".format(className))

    while True:
        try:
            score = float(input("Score of student: "))
            check = str(score)
            if "." in check:
                assert len(check.split(".")[-1]) == 1
            assert 0 <= score <= 100
            break
        except:
            print("Student's score must be a positive number between 0 and 100 inclusive correct to 1 decimal place.")
        
    if score >= 75:
        distinctions.append(name)
    elif score < 50:
        fails.append(name)
   
    scores.append(score)

print("Students who have achieved distinction: {}".format(", ".join(distinctions)))
print("Students who have failed: {}".format(", ".join(fails)))
print("Average score of the class: {}".format(round(sum(scores)/len(scores), 1)))
