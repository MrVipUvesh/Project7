import math

class MathOperations:
    def fact(self, num):
        return math.factorial(num)

    def compount_interest(self, p, r, t):
        amount = p * (1 + r / 100) ** t
        ci = amount - p
        return ci

    def geo_sin(self, num):
        radians = math.radians(num)
        return math.sin(radians)

    def geo_cosine(self, num):
        radians = math.radians(num)
        return math.cos(radians)

    def geo_tan(self, num):
        radians = math.radians(num)
        return math.tan(radians)

    def geo_Isin(self, num):
        radians = math.radians(num)
        return math.asin(radians)

    def geo_Icosine(self, num):
        radians = math.radians(num)
        return math.acos(radians)

    def geo_Itan(self, num):
        radians = math.radians(num)
        return math.atan(radians)

    def geo_shapes(self):
        print("\nArea of Geometric Shapes:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Parallelogram")
        print("6. Trapezoid")
        print("7. Back to menu")
        area = None
        choice = int(input("Choose a shape: "))

        match choice:
            case 1:
                side = float(input("Enter side: "))
                area = side ** 2
            case 2:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
            case 3:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
            case 4:
                radius = float(input("Enter radius: "))
                area = math.pi * radius ** 2
            case 5:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = base * height
            case 6:
                a = float(input("Enter first parallel side: "))
                b = float(input("Enter second parallel side: "))
                height = float(input("Enter height: "))
                area = 0.5 * (a + b) * height
            case _:
                area = None
                print("Invalid choice!")

        if area is not None and area is not 7:
            if choice in range(1, 8):
                if choice == 1 and side <= 0:
                    print("Measurements must be positive.")
                elif choice == 2 and (length <= 0 or width <= 0):
                    print("Measurements must be positive.")
                elif choice == 3 and (base <= 0 or height <= 0):
                    print("Measurements must be positive.")
                elif choice == 4 and radius <= 0:
                    print("Measurements must be positive.")
                elif choice == 5 and (base <= 0 or height <= 0):
                    print("Measurements must be positive.")
                elif choice == 6 and (a <= 0 or b <= 0 or height <= 0):
                    print("Measurements must be positive.")
                else:
                    print(f"Area: {area:.2f} square units")
                    print("========================")