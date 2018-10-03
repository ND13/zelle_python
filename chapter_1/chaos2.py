# File: chaos2.py
# A simple program illustrating chaotic behavior.

def main():
    print('This program illustrates a chaotic function')
    x = float(input("Enter a number between 0 and 1: "))
    y = float(input("Enter a number  between 0 and 1: "))
    print(f"""{x}        {y}
----------------------""")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(f"""{x:.6f}  |  {y:.6f}""")
main()
