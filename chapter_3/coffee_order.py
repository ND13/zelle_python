# coffee_order.py
# calculates the total order of a coffee shipment from Konditorei coffee shop.

def main():
    lbs_of_coffee = float(input("Enter number of pounds for coffee order: "))
    total_cost = (lbs_of_coffee * 10.50) + (lbs_of_coffee * 0.86) + 1.50

    print(f"The total cost for this order is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
