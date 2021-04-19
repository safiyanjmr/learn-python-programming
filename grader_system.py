#!/usr/bin/env python3

def find_grade(mark):
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
    mark = int(input("Enter marks [0 - 100]: "))

    if mark > 100 or mark < 0:
        print("Invalid marks range, please enter marks in [0 - 100]")
    else:
        grade = find_grade(mark)
        print(f"{mark} is letter grade {grade}")


if __name__ == "__main__":
    main()
