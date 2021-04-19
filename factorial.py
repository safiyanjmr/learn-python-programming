#!usr/bin/env python3

def factorial(n):
    if n == 0:
        return 1
    else: return factorial(n-1) * n

def tail_facorial(n, accumulator = 1):
    if n == 0:
        return accumulator
    else:
        return tail_factorial(n-1, accumulator * n)


if __name__ == "__main__":
    main()
