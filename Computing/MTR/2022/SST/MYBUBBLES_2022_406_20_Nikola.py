list_length = int(input("List length: "))
def bubblesort(arr):
    arr = list(set(arr))
    for r in range(1,list_length):
        for p in range(0, list_length - r):
            if arr[p] < arr[p+1]:
                arr[p], arr[p+1] = arr[p+1], arr[p]
    return arr

arr = []
for i in range(5):
    while True:
        try:
            num = int(input("Please input an integer: "))
            break
        except:
            print("Input must be an integer.")
    arr = arr + [num]

print("The sorted list:", bubblesort(arr))


