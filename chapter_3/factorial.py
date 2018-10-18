# factorial.py
# Computes the factorial of a number entered by user

def main():
    print("This will compute the factorial of a given number")

    n = int(input("Please enter a number: "))
    fact = 1

    for i in range(n, 1, -1):
        fact = fact * i

    print(fact)

main()
