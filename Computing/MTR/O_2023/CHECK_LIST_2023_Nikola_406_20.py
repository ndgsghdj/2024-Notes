def split_sentence(word_string) :
    list_sentence = word_string.split()
    return list_sentence

def check_list(word_string, word):
    word_list = split_sentence(word_string)
    if word in word_list:
        return "Yes"

    return "No"
