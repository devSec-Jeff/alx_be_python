income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = income - expenses

projected_savings = float(monthly_savings) * 12 + (float(monthly_savings) * 12 * 0.05)

print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",int(projected_savings))
