#!/usr/bin/env python3

import timeit

def main():
  
    timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    #print(f"List populated in {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    main()
