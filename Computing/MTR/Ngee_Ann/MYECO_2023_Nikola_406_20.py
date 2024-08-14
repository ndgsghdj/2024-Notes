def branch_overview(branch_input):
    return branch_input[0], sum([int(c) for c in branch_input[1:] if branch_input.index(c) % 3 == 0])

def cashiers(raw_data):
    mod_lst = []
    for c in raw_data:
        cashier_prefix = c[0]
        for k in c[1:]:
            if c[1:].index(k) % 3 == 0:
                mod_lst.append(cashier_prefix + k)
    no_bags_lst = []
    for c in raw_data:
        for k in c[1:]:
            if c.index(k) % 3 == 0:
                no_bags_lst.append(k)

    return mod_lst, no_bags_lst

raw_data = []
input_data = ""

while input_data != "0":
    input_data = input("Enter your branch data in the required format (0 to exit):\n")
    raw_data.append(input_data.split(" "))

branches, branch_overview_lst = [branch_overview(c)[0] for c in raw_data], [branch_overview(c)[1] for c in raw_data]

print("The top branch with highest number of recycled bags sold is:\n{} {}".format(branches[branch_overview_lst.index(max(branch_overview_lst))], max(branch_overview_lst)))

mod_lst, no_bags_lst = cashiers(raw_data)

print("The top cashier among all branches is: {} {}".format(mod_lst[no_bags_lst.index(max(no_bags_lst))], max(no_bags_lst)))
