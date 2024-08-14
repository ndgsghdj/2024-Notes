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

