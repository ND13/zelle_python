# change.py
# A program to calculate the value of some change in dollars

def main():
    print("Change Coutner\n")
    print("Please enter the count of each coin type.")

    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = float((quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01))

    print(f"The total of your change is ${total:.2f}")

main()
