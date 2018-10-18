# sphere_1.py
# calculates the volume and surface area of a sphere based on radius

def main():
    radius = float(input("Enter the radius of the sphere: "))
    volume = 4 / 3 * 3.14159 * radius ** 3
    surface_area = 4 * 3.14159 * radius ** 2

    print(f"Volume: {volume:.2f}")
    print(f"Surface Area {surface_area:.2f}")

main()
