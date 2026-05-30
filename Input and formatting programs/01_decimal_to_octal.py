value=int(input("Enter a number : "))

octal=oct(value)
# octal=oct(value)[2::]

    # print(f"{value} Decimal to {value:o} Octal")# this is one way to print this
print(f"{value} Decimal to {octal} Octal")