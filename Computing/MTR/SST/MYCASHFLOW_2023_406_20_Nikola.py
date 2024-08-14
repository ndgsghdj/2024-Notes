days = 7
cashflow = [0] * days
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#input of expenditure or earning for each day of a week
for i in range(days):
    temp = int(input("{} Expenditures / Earnings: ".format(day_names[i])))
    cashflow[i] = temp

sum_cashflow = sum(cashflow)

if sum_cashflow > 0:
    print(sum_cashflow,"(Profit)")
elif sum_cashflow < 0:
    print(-1*sum_cashflow,"(Loss)")
else:
    print(sum_cashflow,"(Break-even)")

