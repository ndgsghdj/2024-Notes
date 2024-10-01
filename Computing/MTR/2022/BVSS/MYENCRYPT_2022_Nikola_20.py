message = input("Enter a message: ")
encrypted_m = ""
for i in range(len(message)):
    if message[i] in "aeiou":
        encrypted_m = encrypted_m + chr(ord(message[i]) - 32)
    elif message[i] == " ":
        encrypted_m = encrypted_m + "&"
    else:
        encrypted_m = encrypted_m + chr(ord(message[i])+3)
print("Encrypted message:", encrypted_m)

def decrypt(s):
    decrypted = ""
    for i in range(len(s)):
        if s[i] in "AEIOU":
            decrypted = decrypted + chr(ord(s[i]) + 32)
        elif s[i] == "&":
            decrypted = decrypted + " "
        else:
            decrypted = decrypted + chr(ord(s[i]) - 3)

    return decrypted

ciphertext = input("Ciphertext: ")
print("Decrypted message: {}".format(decrypt(ciphertext)))
