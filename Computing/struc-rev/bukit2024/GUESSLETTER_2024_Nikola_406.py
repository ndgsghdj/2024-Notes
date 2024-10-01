import random

def select_word(w_list):
    r_num= random.randint(0,len(w_list)-1)
    word = w_list[r_num]
    return word

def check_word(word1, word2):
    return word1 == word2

def check_letter(word, letters):
    new_word = word

    for c in word:
        if c not in letters:
            new_word_list = list(new_word)
            idx = new_word_list.index(c)
            new_word_list[idx] = "_"
            new_word = "".join(new_word_list)

    return new_word

