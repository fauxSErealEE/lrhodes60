#sphere.py
#takes in radius and calculates volume and surface area

import math as math

def main():
    rad = eval(input("Enter sphere radius: "))
    vol = (4.0/3.0) * math.pi * rad**3
    sa = 4 * math.pi * rad**2

    print("The volume is", vol, "and the surface area is", sa)

main()