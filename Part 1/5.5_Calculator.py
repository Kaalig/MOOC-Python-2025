# Write your solution here

nbr1 = int(input("Number 1: "))
nbr2 = int(input("Number 2: "))
operation = str(input("Operation:"))


if operation == "add":
    print(f"{nbr1} + {nbr2} = {nbr1 + nbr2}")

if  operation == "multiply":
    print(f"{nbr1} * {nbr2} = {nbr1 * nbr2}")

if operation == "subtract":
    print(f"{nbr1} - {nbr2} = {nbr1 - nbr2}")
