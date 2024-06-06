flag = True
message = ''
while flag:
    message = input("Enter the message: ").upper()
    message = message.split(" ")
    for x in message:
        if not x.isalpha():
            print("Invalid entry, please input only letters.")
            flag = True
            continue
    else:
        flag = False

encrypted_message = ""
for word in message:
    encrypted_word = ""
    for letter in word:
        if letter == 'Z':
            letter = "A"
        else:
            letter = chr(ord(letter)+1)
        encrypted_word += letter
    encrypted_message = encrypted_message + " " + encrypted_word
    encrypted_message = encrypted_message.lstrip()

print(encrypted_message)
