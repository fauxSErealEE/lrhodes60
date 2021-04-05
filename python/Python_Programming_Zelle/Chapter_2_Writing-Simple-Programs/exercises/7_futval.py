#futval.py

def main():
    pmt = eval(input("Enter period payment: "))
    apr = eval(input("Enter apr: "))
    yrs = eval(input("Enter years: "))
    per = eval(input("Enter number periods: "))

    futval = 0

    for i in range(yrs*per):
        futval = (futval + pmt) * (1 + apr/per)

    print("The future value is:",futval)

main()