#triangle-area2.py

def triArea(a,b,c):
    s = (a + b + c) / 2.0
    area = (s * (s - a) * (s - b) * (s - c))**0.5
    return area

def main():
    a, b, c = eval(input("Enter the three sides of a triangle, separated by a comma: "))
    print("The triangle area is {0:.3f}".format(triArea(a,b,c)))

main()