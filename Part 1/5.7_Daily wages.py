# Write your solution here
hwage = float(input("Hourly wage: "))
work = int(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
     hwage *=2

print(f"Daily wages: {hwage * work} euros")
