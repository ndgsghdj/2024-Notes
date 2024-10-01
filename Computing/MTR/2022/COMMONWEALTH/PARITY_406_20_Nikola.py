def enter_data():
    while True:
        try:
            packet = input("Enter a binary data packet: ")
            for c in packet:
                assert c in "01"
            break
        except:
            print("Data packet should consists of only '0's or '1's.")

    return packet

def count_ones(d):
    return d.count('1') 

def add_bit(d, oddeven):
    new = d
    sum = count_ones(d)
    if oddeven == "even":
        if sum % 2 == 0:
            new += "0"
        else:
            new += "1"

    else:
        if sum % 2 == 1:
            new += "0"
        else:
            new += "1"

    return new

def check_parity(d, oddeven):
    sum = count_ones(d)
    if oddeven == "even":
        return sum % 2 == 0
    elif oddeven == "odd":
        return sum % 2 == 1

packet = enter_data()
oddeven = input("Parity system (odd/even): ").lower()
sendreceive = input("Are you sending or receiving data? ").lower()

if sendreceive == "s":
    new = add_bit(packet, oddeven)
    print("Data packet with parity bit: {}".format(new))
else:
    if check_parity(packet, oddeven):
        print("Data received correctly.")
    elif not check_parity(packet, oddeven):
        print("Data received incorrectly.")


