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
