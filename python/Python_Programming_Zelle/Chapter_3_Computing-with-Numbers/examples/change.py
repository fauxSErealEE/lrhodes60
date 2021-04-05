#change.py

def main():

    print("Change counter")
    print()
    print("Enter amount of each coin type.")
    q = eval(input("Quarters: "))
    d = eval(input("Dimes: "))
    n = eval(input("Nickels: "))
    p = eval(input("Pennies: "))

    total = .25 * q + .1 *d + 0.05 * n + 0.01 * p

    print("The total value is $",total)

main()