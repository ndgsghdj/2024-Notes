def enter_data():
    while True:
        try:
            packet = input("Enter a binary data packet: ")
            for c in packet:
                assert c in "01"
            break
        except:
            print("Data packet should consists of only '0's or '1's.")

