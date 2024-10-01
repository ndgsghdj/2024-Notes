import random
questions = 10
answer_list = [] #1
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions): #2
    num1 = (random.randint (1,50))
    num2 = (random.randint (1,50))
    answer = num1 + num2 #3
    print ("What is", num1, "+", num2, "?")
    user_answer = input()
    if int(user_answer) == answer: #5
        answer_list = answer_list + ["Correct"] #10
        if num1 > 25 and num2 > 25: #4
            total_mark = total_mark + 2
        else:
            total_mark = total_mark + 1
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) #6
for i in range(list_length):
    if answer_list[i] == "Correct": #7
        correct = correct + 1 #8
if correct == 1: #9
    message = "answer."
else:
    message = "answers."
print ("Your total mark is", total_mark, "and you had", correct, "correct", message)

