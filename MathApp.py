#!/usr/bin/env python3
from datetime import datetime
    
def printSpace():
    print()

        
def addNumbers(num1, num2):
    result = num1 + num2
    print(f'The Addition of {num1} and {num2} is',result)
  

def multiplyNumbers(num1, num2):
    result = num1 * num2
    print(f'The Product of {num1} and {num2} is',result)

    
def subtractNumbers(num1, num2):
    result = num1 - num2
    print(f'The Difference of {num1} and {num2} is',result)
    

def divNumbers(num1, num2):
    result = num1 // num2
    print(f'The Division of {num1} and {num2} is',result)


def square(num1, num2):
    result = num1 ** num2
    print(f'The Square Root of {num1} is',result)


def reminder(num1, num2):
    result = num1 % num2
    print(f'The Reminder of {num1} is',result)


def minN(num1, num2):
    if num1 < num2:
        print(f'{num1} is lessthan {num2}')
    elif num2 < num1:
        print(f'{num2} is lessthan {num1}')
    elif num1 == num2:
        print(f'{num2} and {num1} are equal')
    else:
        print('Invalid Input')


def maxN(num1, num2):
    if num1 > num2:
        print(f'{num1} is greater than {num2}')
    elif num2 > num1:
        print(f'{num2} is greater than {num1}')
    elif num1 == num2:
        print(f'{num1} and {num2} are equal')
    else:
        print('Invalid Input')


def selectAll():
    printSpace()
    print('welcome to Math Application')
    print('---------------------------')
    print('Press 1 for Square')
    print('Press 2 for Modules')
    print('Press 3 for Addition')
    print('Press 4 for Division')
    print('Press 5 for Subtraction')
    print('Press 6 for Multiplication')
    print('Press 7 for Maximum')
    print('Press 8 for Minimum')
    

def main():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    selectAll()
    printSpace()
    
    choice = input('Select from (1-8): ')
    if choice == '1' or choice.lower() == 'sq':
        square(num1, num2)
    elif choice == '2' or choice.lower() == 'mod':
        reminder(num1, num2)
    elif choice == '3' or choice.lower() == 'add':
        addNumbers(num1, num2)
    elif choice == '4' or choice.lower() == 'div':
        divNumbers(num1, num2)
    elif choice == '5' or choice.lower() == 'sub':
        subtractNumbers(num1, num2)
    elif choice == '6' or choice.lower() == 'mul':
        multiplyNumbers(num1, num2)
    elif choice == '7' or choice.lower() == 'max':
        maxN(num1, num2)
    elif choice == '8' or choice.lower() == 'min':
        minN(num1, num2)
    else:
        print('Invalid choice!')
        
    choice = input('do u want to continue? (y/n): ')
    if choice.lower() == 'y' or choice.lower() == 'yes':
        printSpace()
        main()
    elif choice.lower() == 'n' or choice.lower() == 'no':
        now = datetime.now()
        print(now)
        print('Thanks for using Math Application')
    else:
        print('Invalid choice!')


if __name__ == "__main__":
    main()


