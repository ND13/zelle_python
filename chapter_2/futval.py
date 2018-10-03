#!/usr/bin/python3.6
# File: futval.py
# A program that computes an investment carried 10 years into future
# 2.8 Exercises: 5, 9

def main():
    print("This program calculates the future value of a 10-year investment.")

    principal = float(input("Enter the principal amount: "))
    apr = float(input("Enter the annualized interest rate: "))
    length = int(input("Enter the length in years of investment: "))
    inflation = float(input("Enter yearly rate of inflation: "))
    apr = apr * .01
    inflation = inflation * .01

    for i in range(length):
        principal = principal * (1 + apr)
        principal = principal / (1 + inflation)
        year = i + 1
        print(f"Year {year}: {principal:.2f}")

    print(f"The amount in {length} years is: {principal:.2f}")

main()
