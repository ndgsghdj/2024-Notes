increased = []

gantries = int(input("Number of gantries: "))

for i in range(gantries):
    while True:
        try:
            expressway = input("Enter name of expressway: ")
            assert len(expressway) <= 20
            for c in expressway:
                assert c.isalpha()
            break
        except:
            print("Name of expressway must have a maximum of 20 characters and must only be made of characters.")

    old = float(input("Enter old rate:"))
    new = float(input("Enter new rate:"))
    change = new - old
    if change > 0:
        increased.append(expressway)

    print("Change is",change)
    
print("Total number of gantries with an increase in the ERP rate: {}".format(len(increased)))
