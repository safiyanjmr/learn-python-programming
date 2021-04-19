#!/usr/bin/env python3

def display(name):
    print("Congratulations", str.title(name), "you can now get addmission in FCP")
    course = input("which course do u apply for? ")

    if course.upper() == 'CSE':
        print(str.title("welcome come to software eng. dept"))
    elif course.upper() == 'CCS':
           print(str.title("welcome to cyber security dept."))
    elif course.upper() == 'CIT':
           print(str.title("welcome to info tech dept."))
    elif course.upper() == 'CSC':
           print(str.title("welcome to computer science dept."))
    else:        
           nsFound()


def main():
    name = input("Enter ur Name: ")
    score = int(input("What is ur Jamb Score: "))

    if score < 180:
        print("Sorry", name, "unfortunately ur not eligible to get addmission in FCP!")
    elif score >= 180 & score <= 200: 
        display(name)
    else:
         print("Invalid Jamb Score")


def nsFound():
    print("\nNo such department found here! ")
    print("we only have 4 Depts. in FCP\n 1. Soft. Engineering\n 2. Cyber Security\n 3. Computer Science\n 4. Information Technology")


if __name__ == "__main__":
    main()



