#futval.py

def main():
    pmt = eval(input("Enter annual payment: "))
    apr = eval(input("Enter apr: "))
    yrs = eval(input("Enter years: "))

    futval = 0

    for i in range(yrs):
        futval = (futval + pmt) * (1 + apr)

    print("The future value is:",futval)

main()