word = input("Please enter your word: ")
word = word.lower() #1
begin_p = word.startswith("p") #2
end_h = word.endswith("h")
contain_e = word.find("e") #3
word_length = len(word) #4
if not begin_p and not end_h and contain_e == -1: #5
    if word_length <= 3: #9
        print("The length of the word is short.") 
    elif word_length <= 10: #6
        print("The length of the word is medium.") 
    else: #7
        print("The length of the word is long.") 
if begin_p:
    print("Invalid. You entered a word that begins with 'p'.")
elif end_h:
    print("Invalid. You entered a word that ends with 'h'.") 
elif contain_e != -1: #8 #10
    print("Invalid. You entered a word that contains 'e'.")
