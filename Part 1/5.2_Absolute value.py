# Write your solution here
user = int(input("Please type in a number: "))

if user < 0:
    user = user * -1
    print(f"The absolute value of this number is {user}")

if user >= 0:
    print(f"The absolute value of this number is {user}")
