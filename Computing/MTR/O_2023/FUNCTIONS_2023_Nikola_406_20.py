def split_sentence(word_string) :
    list_sentence = word_string.split()
    return list_sentence

def check_list(word_string, word):
    word_list = split_sentence(word_string)
    if word in word_list:
        return "Yes"

    return "No"

def reverse_sentence(word_string):
    word_list = split_sentence(word_string)
    reversed = []
    for i in range(len(word_list)-1, -1, -1):
        reversed.append(word_list[i])
    
    return " ".join(reversed)

word_string = input("Please enter a string of words: ")
word = input("Please enter a search word: ")
print("Words split into a list: {}".format(split_sentence(word_string)))
print("The words, reversed: {}".format(reverse_sentence(word_string)))

if check_list(word_string, word) == "Yes":
    print("Inputted word is found in the sentence.")
else:
    print("Inputted word is not found in the sentence.")
