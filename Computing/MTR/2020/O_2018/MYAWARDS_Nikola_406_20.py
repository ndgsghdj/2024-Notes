students = True #7
while students == True:
    comp = int(input("Enter the Computing test score  ")) #2
    math = int(input("Enter the Mathematics test score ")) #1
    joint_score = comp + math
    if comp >= 100 and math >= 100: #7
        print("Student is awarded a gold award")    
    elif comp >= 100 or math >= 100 and joint_score >= 180: #3
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75: #4
        print("Student is awarded a bronze award")
    else:
        print("No award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
    if more_scores == 'N': #5
        students = False #6
    else:
        students = True 
