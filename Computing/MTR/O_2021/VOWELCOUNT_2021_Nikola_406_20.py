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

if vowel_count == 0:
    print("There are no vowels in the word.")
elif vowel_count == 1:
    print("There is one vowel in the word.")
else:
    print("There are {} vowels in the word.".format(vowel_count))
