#!/usr/bin/env python3

"""
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")


my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except KeyError:
    print("Some other problem happened!")
else:
    print("No error occurs")


def myFunc(ages):
    if ages < 18:
        print("Srry u ar not eligible")
    else:
        adults = filter(myFunc, ages)
    for x in adults:
        print("ur elible and ur age is ", x)


def main():
    ages = int(input("Enter ur age: "))
    myFunc(ages)

if __name__ == "__main__":
    main()

"""


