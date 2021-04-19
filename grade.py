#!/usr/bin/env Python3

def marks(mark):

    if mark >= 70 and mark <= 100:
        return 'A'
    elif mark >= 60 and mark < 70:
        return 'B'
    elif mark >= 50 and mark < 60:
        return 'C'
    elif mark >= 40 and mark < 50:
        return 'D'
    else:
        return 'F'


def main():
        mark = input("Enter your marks: ")

        if mark > 100 or mark < 0:
           print("The grade must be less than or equal to 100")
        else:
             marks(mark)
             #print(f"{marks} is letter grade {grade}")


if __name__ == "__main__":
        main()

