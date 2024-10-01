def average(num_list):
    return sum(num_list) / len(num_list)

def user_input():
    print("Welcome to Simple Numbers")
    print("Numbers please.")
    numbers = []
    check = False

    while True:
        numbers = input("Separate each number using spaces: ").split(" ")

        for i in numbers:
            if not(i.isalnum()):
                print("Inputs have to be valid digits.")
                check = True
                break

        if check:
            pass
        else:
            break
            

    return [int(k) for k in numbers]

def main():
    numbers = user_input()
    print("Average: {}".format(average(numbers)))
    print("Maximum: {}".format(max(numbers)))
    print("Minimum: {}".format(min(numbers)))

main()
