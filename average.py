#!usr/bin/env python3

while True:
    try:
        num1 = float(input("Enter Num1: "))
        num2 = float(input("Enter Num2: "))
        num3 = float(input("Enter Num3: "))
        break
    except ValueError:
        print("Please enter a valid number try again!")
result = num1 + num2 + num3 / 3
print("The average of three Numbers is", result)
