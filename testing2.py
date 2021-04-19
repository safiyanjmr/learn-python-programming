#!usr/bin/env python3
from datetime import datetime, timedelta

def question1():
    wscores = {'q1': '1', 'q2': '2', 'q3': '3', 'q4': '4', 'q5': '5'}
    print()
    print('Q1. What HTML stand for:')
    print('------------------------')
    print('1. Hypertext Marking Language')
    print('2. High Marking Language')
    print('3. HyperText MarkUp Language')
    print()
    ans = input("Select from (1-3): ")

    if ans == '1' or ans == '2':
        print('Wrong Answer!')
        choice = input('do u want to continue(y/n): ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            question1()
        elif choice.lower() == 'n' or choice.lower() == 'no':    
            print(f'thanks for participating {name}')
    elif ans == '3':
        remain = [x for x in range(5) if x == 4]
        print()
        print('Correct Answer')
        print('Scores', wscores['q1'])
        print(f'Remain {remain} questions')
        question2()
    else:
        print('Invalid selection')
        choice = input('do u want to continue(y/n): ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            question1()
        elif choice.lower() == 'n' or choice.lower() == 'no':    
            print(f'thanks for participating {name}')
            
            
def question2():
    wscores = {'q1': '1', 'q2': '2', 'q3': '3', 'q4': '4', 'q5': '5'}
    print()
    print('Q2. What CSS stand for: ')
    print('-----------------------')
    print('1. Control Side Scripting')
    print('2. Cascading StyleSheet')
    print('3. Cascading SpreedSheet')
    print()
    ans = input("Select from (1-3): ")

    if ans == '1' or ans == '3':
        print('Wrong Answer!')
        choice = input('do u want to continue(y/n): ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            question2()
        elif choice == 'n' or choice == 'no':    
            print('thanks')
    elif ans == '2':
        remain = [x for x in range(5) if x == 3]
        print()
        print('Correct Answer')
        print('Scores', wscores['q2'])
        print(f'Remain {remain} questions')
        question3()
    else:
        print('Invalid Selection')
        choice = input('do u want to continue(y/n): ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            question2()
        elif choice.lower() == 'n' or choice.lower() == 'no':    
            print('thanks for participating')    


def question3():
    wscores = {'q1': '1', 'q2': '2', 'q3': '3', 'q4': '4', 'q5': '5'}
    print()
    print('Q3. Java is an OOP Language?')
    print('----------------------------')
    print('1. TRUE')
    print('2. FALSE')
    print()
    ans = input("Select from (1-2): ")

    if ans == '2':
        print('Wrong Answer')
        choice = input('do u want to continue(y/n): ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            question3()
        elif choice.lower() == 'n' or choice.lower() == 'no':
            print('thanks')
    elif ans == '1':
        remain = [x for x in range(5) if x == 2]
        print()
        print('Correct Answer')
        print('Scores', wscores['q3'])
        print(f'Remain {remain} questions')
        question4()
    else:
        print('Invalid Selection')
        choice = input('do u want to continue(y/n): ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            question3()
        elif choice == 'n' or choice == 'no':    
            print('thanks for participating')            


def question4():
    wscores = {'q1': '1', 'q2': '2', 'q3': '3', 'q4': '4', 'q5': '5'}
    print()
    print('Q4. What is the Arab name of Algorithm: ')
    print('--------------------------------------')
    print('1. Alkawarisimi')
    print('2. Abduljabbar')
    print('3. Muqabala')
    print()
    ans = input("Select from(1-3): ")

    if ans == '2' or ans == '3':
        print('Incorrect')
    elif ans == '1':
        remain = [x for x in range(5) if x == 1]
        print()
        print('Correct Answer')
        print('Scores', wscores['q4'])
        print(f'Remain {remain} question')
        question5()
        choice = input('do you want to continue(y/n): ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            question4()
        elif choice.lower() == 'n' or choice.lower() == 'no':
            prints('thanks for participating')
    else:
        print('Invalid Selection')        


def question5():
    wscores = {'q1': '1', 'q2': '2', 'q3': '3', 'q4': '4', 'q5': '5'}
    print()
    print('Q5. This language was initially called (Oak) but was renamed (Java) in...')
    print('-------------------------------------------------------------------------')
    print('1. 1995')
    print('2. 1997')
    print('3. 1999')
    print()
    ans = input("Select from(1-3): ")

    if ans == '2' or ans == '3':
        print('Incorrect')
    elif ans == '1':
        remain = [x for x in range(5) if x == 1]
        print()
        print('Correct Answer')
        print('Scores', wscores['q5'])
        result(main)
        choice = input('do you want to continue(y/n): ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            question4()
        elif choice.lower() == 'n' or choice.lower() == 'no':
            prints('thanks for participating')
    else:
        print('Invalid Selection')        

def result():
    print('Congratulations')
    

def main():
    #wscores = {'q1': '1', 'q2': '2', 'q3': '3', 'q4': '4', 'q5': '5'}
    name = input("Enter ur Name to Start Quiz: ")
    #name = name.replace(" ", '\n')
    name = name.title()
    print(f'You are Welcome {name}')
    question1()









if __name__ == "__main__":
    main()

