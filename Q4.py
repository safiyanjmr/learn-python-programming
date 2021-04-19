#!usr/bin/env python3


num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")

if num1 > num2:
        print(num1,"is greater than", num2)
elif num2 > num1:
        print(num2,"is greater than", num1)
elif num2 == num1:
        print(num1, "and", num2, "are equal")
