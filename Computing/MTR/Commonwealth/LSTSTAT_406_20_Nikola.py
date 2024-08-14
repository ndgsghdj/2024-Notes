def lst_3d(lst):
    return [c for c in lst if len(str(c)) == 3]

def lst_even(lst):
    return [c for c in lst if c % 2 == 0]

def even_3d(lst):
    three_digits = set(lst_3d(lst))
    evens = set(lst_even(lst))
    return list(set.intersection(three_digits, evens))

def multiply5(lst):
    return [5*c for c in lst]

def output_msg(output_lst):
    print("The new list is {}".format(",".join([str(c) for c in output_lst])))

while True:
    try:
        lst = input("Enter data separated by ',': ").split(',')
        assert False not in [(int(c)>0) and (int(c) < 999) for c in lst]
        break
    except:
        print("Data must be positive numbers less than or equal to 999.")

choice = input("Enter (1) for 3-digit even list and (2) for multiply by 5 list: ")

if choice == "1":
    output_lst = even_3d([int(c) for c in lst])
else:
    output_lst = multiply5([int(c) for c in lst])

output_msg(output_lst)
