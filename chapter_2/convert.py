#!/usr/bin/python3.6
# File: convert.py
# A simple program converting celsius degrees to fahrenheit
# Exercises 2.8 - 3, 6, 7

def main():
    print("This will convert degress in celsius to fahrenheit.")

    degrees_celsius = int(input("Enter the degrees in celsius: "))
    degress_fahrenheit = 9.0 / 5.0 * degrees_celsius + 32

    print(f"It is {degress_fahrenheit:.1f} degress in fahrenheit outside today")

def main_2():
    print("This will convert degress in celsius to fahrenheit.")

    for i in range(5):
        degrees_celsius = int(input("Enter the degrees in celsius: "))
        degress_fahrenheit = 9.0 / 5.0 * degrees_celsius + 32
        print(f"It is {degress_fahrenheit:.1f} degress in fahrenheit outside today")

def main_3():
    start_celsius = 0

    for i in range(11):
        print(f"""celsius {start_celsius} --- Fahrenheit {9.0 / 5.0 * start_celsius + 32}""")
        start_celsius += 10

main()
main_2()
main_3()
