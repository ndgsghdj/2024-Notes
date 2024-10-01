while True:
    try:
        a = int(input("Enter a denary number: "))
        assert a > 0
        break
    except:
        print("Only positive numbers are accepted as input.")

converted = 0
loop = 0

for _ in range(5):
    while a != 0:
        remainder = a % 2
        converted = converted + remainder*(10**loop)
        a = a // 2
        loop += 1

print("Binary equivalent of {} is {}".format(a, converted))
