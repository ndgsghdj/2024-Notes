from time import sleep

letter = input("Enter a lower case letter to find:")
sentence = input("Enter sentence:").lower() #2
frequency = 0
freqtext = ""
if sentence.find(letter) >= 0: #1
    print("Letter is found at position:")
    while sentence.find(letter) != -1:
        frequency += 1 #3
        idx = sentence.find(letter) #4
        print(idx)
        sentence = sentence[:idx] + "#" + sentence[idx+1:] #9
    if frequency > 5:
        freqtext = "high"
    elif 3 <= frequency <= 5: #5
        freqtext = "moderate"
    else: #6
        freqtext = "low"

    print("The letter occurs at a {} frequency.".format(freqtext)) #10

else: #7
    print("Letter {} is not found".format(letter)) #8
