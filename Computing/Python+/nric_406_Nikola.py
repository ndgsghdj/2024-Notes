def check_digit_nric(nric: str):

    weights = [2,7,6,5,4,3,2]
    remainder_prefix = {
        "ST": "JZIHGFEDCBA",
        "FG": "XWUTRQPNMLK"
    }

    nric_int = [int(x) for x in nric if x.isnumeric()]
    print(nric_int)

    nric_sum= sum([x * weights[nric_int.index(x)] for x in nric_int])

    print(nric_sum)
    if nric[0] == "T" or nric[0] == "G":
        nric_sum += 4
        print(nric_sum)
    nric_sum %= 11
    print(nric_sum)
    for key in remainder_prefix.keys():
        if nric[0] in key:
            check_digits = list(remainder_prefix[key])
            return check_digits[nric_sum]

print(f"{check_digit_nric("T0827027")}")
