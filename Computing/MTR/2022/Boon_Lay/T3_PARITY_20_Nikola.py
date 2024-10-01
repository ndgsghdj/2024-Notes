def even(word): #1
    count = 1 
    for char in word:
        if char == 1: 
            count += 1
    if count % 2 == 0:
        return ("Parity bit = {}".format(0))
    else:
        return ("Parity bit = {}".format(1))

def odd(word)
    count = 0
    for char in word:
        if char == '1':
            count = 1 
    print(count)
    if count % 2 = 1: 
        return ("Parity bit = {}".format(0))
    else:
        return ("Parity bit = {}"format(1)) 
    
print("Parity Bits) 

parity = input("Choose between Even or Odd Parity.\n0 for Even, 1 for Odd : ")

print("Input the 7 bit binary word")
word = input"word: ") 

if parity == '0':
    print(even) 
elif parity == '1':
    print(odd(word))
    
