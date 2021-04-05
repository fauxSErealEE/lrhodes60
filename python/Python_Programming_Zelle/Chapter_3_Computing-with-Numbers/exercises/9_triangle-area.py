#triangle-area.py

import math as math

def main():
    a, b, c = eval(input("Enter all three sides separated by commas: "))
    
    s = float((a + b + c) / 2)
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area is {:0.3f}".format(A))
main()