letter = input("Enter a lower case letter to find:")
sentence = input("Enter sentence:").lower() #2
frequency = 0
if sentence.find(letter) == 0: #1
    print("Letter is found at position:")
    while sentence.find(letter) != -1:
        frequency += 1 #6
        idx = sentence.find(letter) #4
        print(idx)
        sentence = sentence[:idx] + "#" + sentence[idx+1:] #3
    if frequency > 5:
        print("Letter occurs many times")
    elif 3 <= frequency <= 5: #5
        print("Letter occurs some times")
    else:
        print("Letter occurs rarely")
else: #6
    print("Letter {} is not found".format(letter)) #7 #8

