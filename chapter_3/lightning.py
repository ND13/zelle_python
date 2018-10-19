# lightning.py
# calculates the distance of a lightning strike based on time between strike and thunder

def main():
    seconds = float(input("Enter the number of seconds between lightning strike and thunder sound: "))
    speed_sound = 1100.00
    mile = 5280.00

    distance = (speed_sound * seconds) / mile

    print(f"The lightning strike is {distance:.2f} miles away")

if __name__ == '__main__':
    main()
