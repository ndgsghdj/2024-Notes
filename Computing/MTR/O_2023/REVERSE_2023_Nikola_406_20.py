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

