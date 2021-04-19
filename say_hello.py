#!/usr/bin/env python3

def say_hello(name):
    name = ['Zainab', 'Muhd', 'Haidar']
    if name == name[0]:
        print(name[0])
    else:
        print(name[1])

        
def main():
    name = input("Enter your name: ")
    say_hello(name)

  
if __name__ == "__main__":
    main()

