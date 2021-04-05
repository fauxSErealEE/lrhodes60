#quadratic.py

import math #Math Library

def main():

    a, b, c = eval(input("Enter coefficients separated by commas (a, b, c): "))
    discRoot = math.sqrt(b**2 - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a * c)
    root2 = (-b - discRoot) / (2 * a * c)

    print()
    print("The solutions are:",root1,root2)

main()