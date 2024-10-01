digits = list("0123456789")
phone_numbers = []
no_numbers = int(input("Number of phone numbers: "))

for i in range(no_numbers):
    while True:
        try:
            digits_remaining = digits
            mobile = input("What is the worker's mobile phone number? ")
            if len(mobile) != 8:
                print("Phone number must be 8 digits long.")
                continue
            for c in mobile:
                assert c in digits
                digits_remaining.pop(digits_remaining.index(c))
            assert digits_remaining == []
            break
        except:
            print("Phone number must comprise of all digits.")

    phone_numbers.append(mobile)

