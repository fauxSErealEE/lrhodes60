#pizza.py

import math as math

def main():
    diam = eval(input("Enter pizza diameter in inches: "))
    price = eval(input("Enter price of pizza: "))

    area = math.pi * (diam/2.0)**2
    cost = price / area

    print("The cost per sq in of pizza is ${:0.2f}".format(cost))

main()