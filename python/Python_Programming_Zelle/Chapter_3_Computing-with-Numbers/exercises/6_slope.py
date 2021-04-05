#slope.py

import math as math

def main():

    x1, y1 = eval(input("Enter first point: "))
    x2, y2 = eval(input("Enter second point: "))

    if (x2 - x1) == 0:
        print("undefined slope")
    else:
        num = y2 - y1
        den = x2 - x1
        slope = float(num / den)
        print("The slope is",slope)

main()