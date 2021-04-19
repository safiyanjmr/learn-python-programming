#!usr/bin/env python3

while True:
    try:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        break
    except ValueError:
        print("Invalid number entry")
if num1 > num2:
        print(num1,"is greater than", num2)
elif num2 > num1:
        print(num2,"is greater than", num1)
elif num2 == num1:
        print(num1, "and", num2, "are equal")
else:
        print("HelloWorld")
