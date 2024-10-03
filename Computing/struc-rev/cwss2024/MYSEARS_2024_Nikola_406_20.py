tries = 5
for x in range(tries):
    while True:
        try:
            strg = input("Enter string: ")
            char = input("Enter character: ")
            assert strg != "" and char != ""
            break
        except:
            print("Invalid input. Please re-enter")
