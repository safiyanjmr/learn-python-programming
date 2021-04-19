#!usr/bin/env python3

yearlyInterestRate = float (input("Enter Yearly Interest Rate: "))
numberOfYears = float (input("Enter Number of Years: "))
loanAmount = float (input("Enter Loan Amount: "))

monthlyInterestRate = yearlyInterestRate / 1200
monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))

print("Students Loan Payment")
print(yearlyInterestRate)
print(numberOfYears)
print(loanAmount)
print("The Monthly Payment is ", round(monthlyPayment, 3))                                                 
#print("The total payment is ", totalPayment)
