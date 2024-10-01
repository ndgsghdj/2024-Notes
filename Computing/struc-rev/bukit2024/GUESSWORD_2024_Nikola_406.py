import random

def select_word(w_list):
    r_num= random.randint(0,len(w_list)-1)
    word = w_list[r_num]
    return word

def check_word(word1, word2):
    return word1 == word2
