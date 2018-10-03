# quadratic.py
# Computes the real roots of a quadratic equation.
# Illustrates the use of math library
# Note: This program crashes if the equation doesn't have real roots

import math

def main():
    print("This program finds the real solutions to a quadratic")

    coefficients = input("Please enter the coefficients (a, b, c): ").split(',')
    coefficients = [int(i) for i in coefficients]

    disc_root = math.sqrt(coefficients[1] * coefficients[1] - 4 * coefficients[0] * coefficients[2])
    root_1 = (-coefficients[1] + disc_root) / (2 * coefficients[0])
    root_2 = (-coefficients[1] - disc_root) / (2 * coefficients[0])

    print(f"\nThe solutions are: {root_1}, {root_2}")

main()
