#distance.py

import math as math

def main():
    x1, y1 = eval(input("Enter first point: "))
    x2, y2 = eval(input("Enter second point: "))

    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance is",dist)

main()