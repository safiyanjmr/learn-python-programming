#!usr/bin/env python3


def main():
    name = input("Enter ur Name to Start Quiz: ")
    ans = input("TRUE or FALSE: Python was released in 1991:\n")

    if ans == "TRUE":
        print('Correct')
    elif ans == "FALSE":
        print('Wrong')
    elif ans != ("TRUE" or "FALSE"):
         print('Please answer TRUE or FALSE')
         print('Bye')



if __name__ == "__main__":
    main()
