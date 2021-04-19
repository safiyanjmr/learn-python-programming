#!/usr/bin/env python3


'''def display(name):
    print("welcome")
'''


def invalidScore():
    print('the score range must be [1 - 400]')


def tryNext(name):
    print(f'Sorry {str.title(name)} u ar not eligible to get addmission in FCP')


def main():

    choice = "y"
    while choice.lower() == "y" or choice.lower() == "yes":
        dept = ['Software Engineering', 'Cyber Security', 'Computer Science', 'Information Technology']
        nums = [1, 2, 3, 4]
        name = input("Enter ur Name: ")
        score(name, dept, nums)

def score(name, dept, nums):
    score = int(input("Enter ur Jamb Score: [180 - 400]: "))

    if score > 400 or score < 0:
        invalidScore()
    elif score >= 180 and score <= 200:
            a = dept.pop(3)
            n1 = nums.pop(0)
            print(f'\nCongratulations {str.title(name)} u have only 1 choice')
            print(n1, a)
    elif score >= 201 and score <= 220:
            b = dept.pop(3)
            c = dept.pop(2)
            n1 = nums.pop(0)
            n2 = nums.pop(1)
            print(f'\nCongratulations {name} u have 2 choice \n1 {b}\n2 {c}')
    elif score >= 221 and score <= 240:
            d = dept.pop(3)
            e = dept.pop(2)
            f = dept.pop(1)
            n3 = nums.pop(0)
            n2 = nums.pop(1)
            n1 = nums.pop(1)
            print(f'\ncongratulations {str.title(name)} u have 3 choice \n1 {d}\n2 {e}\n3 {f}')
    elif score >= 241 and score <= 400:
            g = dept.pop(3)
            h = dept.pop(2)
            i = dept.pop(1)
            j = dept.pop(0)
            n3 = nums.pop(0)
            n2 = nums.pop(0)
            n1 = nums.pop(0)
            n0 = nums.pop(0)
            print(f'\ncongratulations {str.title(name)} u have multiple choice \n1 {g}\n2 {h}\n3 {i}\n4 {j}')
    else:
       tryNext(name)

    print()
    choice = input("do u want to continue (y/n): ")
    print("Bye!")


if __name__ == "__main__":
    main()


