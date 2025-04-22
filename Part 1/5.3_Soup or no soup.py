# Write your solution here

price = 5.9

name = input("Please tell me your name: ")

if name == "Jerry":
    print("Next please!")
else:
    portion = int(input("How many portions of soup? "))
    total = price * portion
    print(f"The total cost is {total}")
    print("Next please!")
