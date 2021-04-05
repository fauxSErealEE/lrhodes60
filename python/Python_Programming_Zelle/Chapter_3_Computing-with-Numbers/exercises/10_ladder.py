#ladder.py

import math as math

def main():
    h, ang_deg = eval(input("Enter height (in feet) and angle (in degrees) for ladder: "))
    ang_rad = float(ang_deg * math.pi / 180)

    if (ang_rad == 0) | (ang_rad == math.pi):
        print("Angle was zero, no ladder needed")
    elif (h == 0):
        print("Height was zero, no ladder needed")
    else:
        len = math.ceil(h / math.sin(ang_rad))
        print("The length of ladder needed is",len)
main()