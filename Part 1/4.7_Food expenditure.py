# Write your solution here

cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
cost_week = float(input("How much money do you spend on groceries in a week? "))
weekly = cost_week + (lunch * cafeteria)
daily = weekly / 7

print(f"Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")
