#!usr/bin/env python3

parts = float(input("Enter parts: "))
labor = float(input("Enter labor: "))
salesTax = 6.27
total = parts + labor + salesTax

print("\n    AJAX AUTO REPAIR")
print("    SERVICE INVOICE")
print("PARTS     ", parts)
print("LABOR     ", labor)
print("SALESTAX  ", salesTax)
print("TOTAL     ", round (total, 2))
print("\nThanks for Your patronage!")

