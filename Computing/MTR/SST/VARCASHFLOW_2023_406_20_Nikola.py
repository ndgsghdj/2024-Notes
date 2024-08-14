days = 7
weeks = 2
cashflow = [0] * days * weeks
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for j in range(weeks):
    print("Week {}".format(j))
    for i in range(days):
        temp = int(input("{} Expenditures / Earnings: ".format(day_names[i])))
        cashflow[i + j*7] = temp

#input of expenditure or earning for each day of a week

sum_cashflow = sum(cashflow)

if sum_cashflow > 0:
    print(sum_cashflow,"(Profit)")
elif sum_cashflow < 0:
    print(-1*sum_cashflow,"(Loss)")
else:
    print(sum_cashflow,"(Break-even)")

print(min(cashflow), "(Smallest earnings entry of the two weeks)")
