#!/usr/bin/env pyhton3

x = int(input("Please Enter an Integer: "))

if x < 0:
        x = 0
        print("Negative change to Zero")
elif x == 0:
        print("Zero")
elif x == 1:
        print("Single")
else:
        print("More")
