month_expense = {'January':2200,'February':2350,'March':2600,'April':2130,'May':2190}
month = list(month_expense.keys())
expense = list(month_expense.values())

print('1. Number of extra dollars spent in February compared to January.')

extra = expense[1]-expense[0]
print('Extra is ',extra) 

quarter_expenses = []
print('2. Total expense for the first quarter.')
for i in range(0,3):
    amount = expense[i]
    quarter_expenses.append(amount)
total = sum(quarter_expenses)
print('Total expense in first quarter is ',total)