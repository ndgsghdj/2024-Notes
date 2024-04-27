from string import ascii_lowercase as alphabet

def shift(char):
    if not char.isalpha() or not char.islower():
        return char

    return alphabet[(alphabet.index(char.lower())+1)%26]

def encrypt(message, positions):
    encrypted = message
    for _ in range(1, positions+1):
        encrypted = ''.join([shift(c) for c in encrypted])
    return encrypted

def shift_up(char):
    if not char.isalpha() or not char.islower():
        return char
    return alphabet[(alphabet.index(char.lower())-1)%26]

def decrypt(ciphertext, positions):
    decrypted = message
    for _ in range(1, positions+1):
        decrypted = ''.join([shift_up(c) for c in decrypted])
    return decrypted

# UI
while True:
    try:
        choice = input("What would you like to do? \n 1. Encrypt a message [Enter 'E'] \n 2. Decrypt a message [Enter 'D']\n")
        assert choice.lower() == 'e' or choice.lower() == 'd'
        break
    except:
        print("Please enter either 'E' or 'D'.")
        choice = input("What would you like to do? \n 1. Encrypt a message [Enter 'E'] \n 2. Decrypt a message [Enter 'D']\n")

    # 1m allow user to input their choice to input their choice + correct validation

if choice.lower() == "e":
    message = input("Please enter your message:\n") # 1m allow user to enter message
    positions = input("Please enter the number of positions you would like to shift the letters in your message.\n")   # 1m allow user to enter the number of positions + correct validation
    while True:
        try:
            positions = int(positions)
            assert positions > 0
            break
        except:
            positions = input("Number of positions must be a positive integer! Please re-enter: \n")
    print("Encrypted message: " + encrypt(message, positions))  # 1m correctly encrypt()

if choice.lower() == "d":
    message = input("Please enter your ciphertext:\n")
    positions = input("Please enter the number of positions you would like to shift the letters in your message.\n")
    while True:
        try:
            positions = int(positions)
            assert positions > 0
            break
        except:
            positions = input("Number of positions must be a positive integer! Please re-enter: \n")
    print("Decrypted message: " + decrypt(message, positions))  # 2m correctly decrypt() and display decrypted text

