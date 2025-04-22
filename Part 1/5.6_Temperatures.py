# Write your solution here
temperature = int(input("Please type in a temperature (F): "))
converted = (temperature - 32) * 5/9

print(f"{temperature} degrees Fahrenheit equals {converted} degrees Celsius")

if converted < 0:
    print("Brr! It's cold in here!")
