#!/usr/bin/env python3

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
    choice = ''
    result = num1 // num2
    print(f'The Division of {num1} and {num2} is',result)


def square(num1, num2):
    result = num1 ** num2
    print(f'The Square Root of {num1} is',result)


def reminder(num1, num2):
    result = num1 % num2
    print(f'The Reminder of {num1} is',result)


def main():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    printSpace()
    selectAll()
    printSpace()
    
    choice = input(': ')
    if choice == '1' or choice.lower() == 'sq':
        square(num1, num2)
    elif choice == '2' or choice.lower() == 'mod':
        reminder(num1, num2)
    elif choice == '3' or choice.lower() == 'add':
        addNumbers(num1, num2)
    elif choice == '4' or choice.lower() == 'div':
        divNumbers(num1, num2)
    elif choice == '5' or choice.lower() == 'sub':
        subractNumbers(num1, num2)
    elif choice == '6' or choice.lower() == 'mul':
        multiplyNumbers(num1, num2)


def printSpace():
    print()


def selectAll():
    print('Press 1 for Square')
    print('Press 2 for Modules')
    print('Press 3 for Addition')
    print('Press 4 for Division')
    print('Press 5 for Subtraction')
    print('Press 6 for Multiplication')
    



if __name__ == "__main__":
    main()
