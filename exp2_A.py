def is_right_triangle(side1, side2, side3):
    if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
        return True
    else:
        return False
    
side1 = float(input("Enter the length of side1: "))
side2 = float(input("Enter the length of side2: "))
side3 = float(input("Enter the length of side3: "))

if is_right_triangle(side1, side2, side3):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")