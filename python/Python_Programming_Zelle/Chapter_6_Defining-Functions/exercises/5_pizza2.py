#pizza2.py

import math as math

def pizzaArea(diam):
    area = ((0.5 * diam)**2) * math.pi 
    return area

def pricePerSqInch(diam,price):
    area = pizzaArea(diam)
    sqInPrice = price / area
    return sqInPrice

def main():
    diameter = eval(input("How big is the pizza (diam)? "))
    price = eval(input("How much is the pizza? "))

    sqInPrice = pricePerSqInch(diameter, price)

    print("The price per square inch of pizza is ${0:.2f}".format(sqInPrice))

main()