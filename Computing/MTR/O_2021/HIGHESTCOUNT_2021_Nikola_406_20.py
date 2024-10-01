words = []
words_2 = []
vowel_counts = []
vowel_counts_2= []

for _ in range(5):
    word = ""

    while True:
        try:
            word = input("Please enter a word: ")
            for c in word:
                assert c.isalpha()
            break
        except:
            print("Word must only contain letters.")

    word = word.lower()

    vowel_count = 0

    for c in word:
        if c in "aeiou":
            vowel_count += 1

    if vowel_count > 2:
        words_2.append(word)
        vowel_counts_2.append(vowel_count)

    words.append(word)
    vowel_counts.append(vowel_count)

highest_vowel_word = ""

for i in range(5):
    if vowel_counts[i] == max(vowel_counts):
        highest_vowel_word = words[i]
        print("Word with the highest number of vowels: {}".format(highest_vowel_word))
        break

vowel_counts = [str(k) for k in vowel_counts]

print("Words with more than 2 vowels: {}".format(", ".join(words_2)))
print("Total number of vowels in all 5 words: {}".format(", ".join(vowel_counts)))

