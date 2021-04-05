#fibonacci.py

def main():
    n = eval(input("Enter n to Fibonacci index: "))
    currFibNum = 1
    prevFibNum = 1
    if(n == 1) | (n == 2):
        print("The Fibonacci number is",currFibNum)
    else:
        for i in range(3,n+1,1):
            temp = currFibNum + prevFibNum
            prevFibNum = currFibNum
            currFibNum = temp
        print("The Fibonacci number is",currFibNum)
    
main()