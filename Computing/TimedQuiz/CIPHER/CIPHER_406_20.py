from string import ascii_lowercase as alphabet

def shift(char):    # 1m function signature and return a string
    if not char.isalpha() or not char.islower(): # 1m check if islower()
        return char

    return alphabet[(alphabet.index(char.lower())+1)%26] # 1m check for boundary
    # 1m correct shifting

    '''
    result = ''
    if char == 'z':
        return 'a'
    if char.islower():
        return chr(ord(char)+1)
    return char
    '''

def encrypt(message, positions):    # 1m function signature with correct parameter
    encrypted = message # 1m initialize variable for returned output
    for _ in range(1, positions+1): # 2m iterating through characters of message and shift char positions number of times
        encrypted = ''.join([shift(c) for c in encrypted])  # 2m call shift()
    return encrypted    # 1m return the message

def shift_up(char):
    if not char.isalpha() or not char.islower():    # 1m checking correct boundary
        return char
    return alphabet[(alphabet.index(char.lower())-1)%26]    # 1m correctly shift upward

def decrypt(ciphertext, positions):
    decrypted = message
    for _ in range(1, positions+1):
        decrypted = ''.join([shift_up(c) for c in decrypted])   # 1m call shift_up()
    return decrypted


