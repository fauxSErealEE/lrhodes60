#chaos2.py

def main():
    x, y = eval(input("Enter two numbers between 0 and 1 separated by a comma: "))
    print("index {0:10} {1:10}".format(str(x).center(11),str(y).center(9)))

    print("-------------------------")
    for i in range(1,10,1):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{0:5} {1:10.6f} {2:10.6f}".format(str(i).center(5),x,y))
main()