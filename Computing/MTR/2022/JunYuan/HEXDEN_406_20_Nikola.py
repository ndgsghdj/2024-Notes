def hextoden(a):
    converted = 0
    hex_sys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    a = a[::-1] #1
    
    for i in range(len(a)):
        value = hex_sys.index(a[i])
        print(f"{value=}")
        converted = converted + value*(16**i) #10
        print(f"{converted=}")
    return converted
    
def dentohex(a): #2
    converted = ""
    hex_sys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"] #9

    while a != 0:
        remainder = a % 16 #8
        converted = hex_sys[remainder] + converted
        a = a // 16 #3
    return converted
        
choice = input("Enter H to convert denary to hex \n\
Enter D to convert hex to denary\n\
Enter Q to Quit: ").upper()
    
while choice != 'Q': #5
    user = input("\nEnter the number to be converted: ")
        
    if choice == 'H':
        hex_num = dentohex(int(user)) #7
        print("Hexadecimal of", user, "is", hex_num, ".")
        
    if choice == 'D':  #4
        den_num = hextoden(user.upper())
        print("Denary of", user.upper(), "is", den_num, ".")

    choice = input("\nEnter H, D or Q: ").upper() 

print("Program ends.") #6
