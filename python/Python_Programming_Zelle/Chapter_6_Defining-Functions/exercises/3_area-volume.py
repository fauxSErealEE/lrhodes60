#area-volume.py

import math as math

def sphereArea(radius):
    sa = 4 * math.pi * radius**2
    return sa

def sphereVolume(radius):
    vol = (4.0/3.0) * math.pi * radius**3
    return vol

def main():
    radius = eval(input("Enter sphere radius: "))
    sa = sphereArea(radius)
    vol = sphereVolume(radius)

    print("The sphere volume is {0:.3f} and the surface area is {1:.3f}".format(vol,sa))

main()