# sphere_2.py
# calculates the price per square inch of circular pizza using price and diameter

def main():
    price = float(input("Enter the price for your pizza: $"))
    diameter = float(input("Enter the diameter of the pizza: "))
    radius = diameter / 2
    area = 3.14159 * radius ** 2

    price_per_sq_inch = price / area

    print(f"The price per square inch of pizza is ${price_per_sq_inch:.2f}")

if __name__ == '__main__':
    main()
