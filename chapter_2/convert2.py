#!/usr/bin/python3.6
# File: convert2.py
# This program converts degress in fahrenheit to degress in celsius

def main():
    print("This program will convert degress in celsius to degress in fahrenheit.")

    degress_c = float(input("Enter the degress in celsius: "))
    degress_f = degress_c * 9/5 + 32

    print(f"The degress in fahrenheit: {degress_f:.1f}")

main()
