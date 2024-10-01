while True:
    try:
        ca1, sa1, ca2 = input().split()
        assert 0 <= int(ca1) <= 100
        assert 0 <= int(ca2) <= 100
        assert 0 <= int(sa1) <= 100
        break
    except:
        print("Marks must be between 0 and 100.")

grades = ["A1", "A2", "B3", "B4"]
cutoff = [75, 70, 65, 60]

ca1 = int(ca1)
ca2 = int(ca2)
sa1 = int(sa1)

overall = 0.4 * (0.3 * ca1 + 0.7 * sa1) + 0.4 * 0.3 * ca2

for i in range(4):
    needed = round((cutoff[i] - overall) / 0.6 / 0.7, 1)
    print(needed)
    remarks = "Can divert"

    if needed >= 1.2 * sa1:
        remarks = "More time"
    elif needed >= 0.8 * sa1:
        remarks = "Maintain"

    if needed > 100:
        needed = "Not obtainable"
    print("{} : {} ({})".format(grades[i], needed, remarks))

