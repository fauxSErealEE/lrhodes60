#cubes.py

def main():
    n = eval(input("Enter numbers to sum: "))
    if (n < 0):
        print("n was less than zero, assumed absolute value")
        n = n* (-1)
    
    sum = 0
    for i in range(1,n+1,1):
        sum = sum + (i**3)

    print("The num of the first",n,"numbers is",sum)
main()