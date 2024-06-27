# UPC-A Practice

def check_digit(code: str):
    result = 0
    sum_odd = sum([int(k) for k in code if code.index(k) % 2 == 0])
    result = sum_odd * 3
    sum_even = sum([int(k) for k in code if code.index(k) % 2 != 0])
    result += sum_even
    result = str(result)
    if result[-1] == '0':
        return 0
    else:
        return 10 - int(result[-1])

def validate_code(code: str):
    if int(code[-1]) != check_digit(code):
        return False
    else:
        return True

# Singapore NRIC (mod-11)

