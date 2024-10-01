n1 = 0
n2 = 1
fib_terms = []

while True:
    try:
        nterms = int(input("Number of terms: "))
        assert nterms > 0
        break
    except:
        print("Number of terms must be a positive integer.")
    

for i in range(nterms):
    print(n1)
    fib_terms.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth

print("Fibonacci terms: {}".format(fib_terms))

check_integer = int(input("Check if positive integer is in the first hundredth terms of the Fibonacci sequence: "))

n1 = 0
n2 = 1
fib_terms = []

for i in range(nterms):
    print(n1)
    fib_terms.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth

if check_integer in fib_terms:
    print("{}".format(check_integer))
else:
    pass
