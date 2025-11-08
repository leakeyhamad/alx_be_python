user_monthly_income = int(input('Enter your monthly income: '))
user_total_monthly_expenses = int(input('Enter your total monthly expenses: '))
user_monthly_savings = user_monthly_income - user_total_monthly_expenses
user_projected_savings = user_monthly_savings * 12 + (user_monthly_savings * 12 *0.05)

print(f'Your monthly savings are ${user_monthly_savings}.')
print(f'Projected savings after one year, with interest, is: ${user_projected_savings}.')