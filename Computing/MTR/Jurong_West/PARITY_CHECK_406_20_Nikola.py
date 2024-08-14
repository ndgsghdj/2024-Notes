#Task 4#

def odd_parity(bits):
    if bits % 2 == 1:
        return True
    else:
        return False

def even_parity(bits):
    if bits % 2 == 0:
        return True
    else:
        return False

def clean_data(raw_data):
    cleaned_data = ""
    for c in raw_data:
        if c.isdigit():
            cleaned_data += c

    return cleaned_data

def validate_data(raw_data):

    digits = clean_data(raw_data)
    for c in digits:
        if c not in ['0', '1']:
            return 'Invalid'

    return 'Valid'

print("*** PARITY CHECK SYSTEM! ***")
print("E - Even Parity\nO - Odd Parity")

while True:
    try:
        choice = input("Enter Choice (E or O):\n").upper()
        assert choice == "E" or choice == "O"
        break
    except:
        print("Invalid option! Choice should either be 'E' or 'O'.")

raw_data = input("Please enter your data for checking: ")

if validate_data(raw_data) == "Invalid":
    print("Invalid input")
    pass
else:
    cleaned_data = clean_data(raw_data)
    cleaned_data = [int(c) for c in cleaned_data.split()]
    bits = sum(cleaned_data)

    if choice == "E":
        check = even_parity(bits)
    else:
        check = odd_parity(bits)

    if check:
        print("No error detected")
    else:
        print("Error detected")
