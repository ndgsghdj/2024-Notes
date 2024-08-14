checksum = "AZYXUTSRPMLKJHGEDCB"
weights = [9, 4, 5, 4, 3, 2] #2
total = 0

reg_plate = input("Registration Plate: ").lower()

prefix_length = 0
while not(reg_plate[prefix_length].isdigit()): #4
    prefix_length += 1
if prefix_length > 1:
    letter_1 = ord(reg_plate[prefix_length-2].upper())-64 #1
    letter_2 = ord(reg_plate[prefix_length-1].upper())-64 #5
    total += letter_1 * weights[0]
    total += letter_2 * weights[1]
else:
    letter = ord(reg_plate[1].upper())-64
    total += letter * weights[1]

mainbody = reg_plate[prefix_length:-1] #6
mainbody = mainbody + "0"*(4-len(mainbody))
weight_counter = 2
for n in mainbody:
    total = total + int(n) * weights[weight_counter] #9
    weight_counter += 1 #7

rem = total % 19
if checksum[rem].lower() == reg_plate[-1]: #3 #8 #10
    print("Checksum passed.")
else:
    print("Checksum failed.")
