# molecular_weight.py
# caluclates the molecular weight of a hydrocarbon based on number hydrogen, carbon and oxygen atoms

def main():
    num_hydro = float(input("Enter the number of hydrogen: "))
    num_carb = float(input("Enter the number of carbon: "))
    num_oxy = float(input("Enter the number of oxygen: "))
    hydro = 1.0079
    carbon = 12.011
    oxygen = 15.9994

    molecular_weight = (num_hydro * hydro) + (num_carb * carbon) + (num_oxy * oxygen)

    print(f"The molecular weight of this hydrocarbon is {molecular_weight:.2f} g/mol")

if __name__ == '__main__':
    main()
