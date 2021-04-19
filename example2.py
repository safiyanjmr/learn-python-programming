#!bin/usr/env python3

def fBank(bvn, bankName):
    f = bankName.pop(0)
    print(f'{f} BVN')
    print(bvn)


def accBank(bvn, bankName):
    a = bankName.pop(1)
    print(f'{a} BVN')
    print(bvn)


def gtBank(bvn, bankName):
    g = bankName.pop(2)
    print(f'{g} BVN')
    print(bvn)


def zBank(bvn, bankName):
    z = bankName.pop()
    print(f'{z} BVN')
    print(bvn)

    
def nsFound():
    print('Error no such bvn found in the database!')

def main():
    choice = "y"
    while choice.lower() == "y" or choice.lower() == "yes":
        bankName = ['FirstBank', 'AccessBank', 'GTBank', 'Zenith Bank']

        bvn = input("Enter ur Bvn Number: ")
  
        if bvn.startswith("22") and len(bvn) == 11:
            fBank(bvn, bankName)
        elif bvn.startswith("23") and len(bvn) == 11:
            accBank(bvn, bankName)
        elif bvn.startswith("24") and len(bvn) == 11:
            gtBank(bvn, bankName)
        elif bvn.startswith("25") and len(bvn) == 11:
            zBank(bvn, bankName)
        elif len(bvn) != 11:    
            print('bvn must be 11 digits')
        else:
            nsFound()

        print()
        choice = input("Enter again?  (y/n): ")
        print()
        print("Bye!")

    
if __name__ == "__main__":
    main()


