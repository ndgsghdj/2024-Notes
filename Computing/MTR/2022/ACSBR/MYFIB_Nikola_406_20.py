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
