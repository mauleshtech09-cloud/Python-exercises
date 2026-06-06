# Practice Problem: Display a large number as currency, including a dollar sign, commas for thousands, and two decimal places.

# Exercise Purpose: Financial applications require strict formatting. This exercise combines three concepts: prefixing, grouping (using commas), and precision to create a professional-grade money display.

money=float(input("Enter Amount: "))

print(f"Amount = ${money:,.2f}")