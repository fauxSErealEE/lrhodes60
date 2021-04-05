#enter-avg.py

def main():
    n = eval(input("How many numbers to average: "))
    if (n < 0):
        print("Entered negative number, used absolute value")
        n = n * (-1)

    sum = 0
    for i in range(1,n + 1,1):
        next = eval(input("Enter next number: "))
        sum = sum + next

    avg = float(sum / n)
    print("The average of entered numbers is",avg)
main()