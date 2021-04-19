#!/usr/bin/env python3
from getpass import getpass


def space():
    print()

user = {'fName': 'Zainab', 'sName': 'Muhd', 'lName': 'Haidar'}
pscd = {'Zainab': '5tR0ng', 'Muhd': 'Pa55', 'Haidar': 'y3S' }

choice = "y"
while choice.lower() == "yes" or choice.lower() == "y":
    userName = input('Enter ur userName: ')
    passCode = input('Enter ur passCode: ')

    if userName == user['fName'] and passCode == pscd['Zainab']:
        space()
        print(f'Welcome to the Admin Panel {userName}')
        print('u have privellege to')
        print('1. Add User')
        print('2. Update User')
        print('3. Search User')
        print('4. Delete User')
    elif userName == user['sName'] and passCode == pscd['Muhd']:
        space()
        print(f'Welcome to the Admin Panel {userName}')
        print('u have 3 privellege')
        print('1. Add User')
        print('2. Update User')
        print('3. Search User')
    elif userName == user['lName'] and passCode == pscd['Haidar']:
        space()
        print(f'Welcome to the Admin Panel {userName}')
        print('u have 2 privellege')
        print('1. Add User')
        print('2. Update User')
    elif userName != user or passCode != pscd:
        space()
        print(f'Sorry {userName} ur name is not in the database!')
    else:
        print('Something went wrong!!!')

    print()
    choice = input('do u want to continue (y/n): ')
    print(f'Bye! {userName}')

