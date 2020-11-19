'''Given that expenses for some months are listed below
i. January- 2200
ii. February - 2350
iii. March - 2600
iv. April - 2130
v. May - 2190

Based on the data above, find:
1. Number of extra dollars spent in February compared to January.

2. Total expense for the first quarter.

3. Find if exactly 2000 was spent in any month

4. New expense list when that of June is added - 1980 dollars

5. New expense list when a refund is made from an item purchased in April
'''


month_expense = {'January':2200,'February':2350,'March':2600,'April':2130,'May':2190}
month = list(month_expense.keys())
expense = list(month_expense.values())

print('\n\t\t1. Number of extra dollars spent in February compared to January.')

extra = expense[1]-expense[0]

print('\nExtra dollars spent in February is ',extra) 

quarter_expenses = []

print('\n\n\t\t2. Total expense for the first quarter.')

for i in range(0,3):

    amount = expense[i]

    quarter_expenses.append(amount)

total = sum(quarter_expenses)

print('\nTotal expense in first quarter is $',total)

print('\n\n\t\t3. Find if exactly 2000 was spent in any month')

if 2000 in expense:
    print('\nYes, exactly 2000 was spent in a certain month')

else: 
    print('\nNo month had an exact expense of 2000')

print('\n\n\t\t4. Add June to expense list')

month_expense['June'] = 1980

print('Updated expense list after adding the expense of June is :')
for key , value in month_expense.items():
    print('\n-',key,'--',value)

print('\n\n\t\t5. Make amends to the expense in April')

month_expense['April'] = 2130 - 2005

print('Updated expense list after refund is:')
for key , value in month_expense.items():
    print('\n-',key,'--',value)