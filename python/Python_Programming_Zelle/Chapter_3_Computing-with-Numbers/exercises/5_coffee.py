#coffee.py

def main():
    pnds = eval(input("Amount purchased (in lbs): "))

    cost_lbs = 10.50
    ship_fixed = 1.50
    ship_lbs = 0.86
    tot_cost = (cost_lbs + ship_lbs) * pnds + ship_fixed

    print("Total cost is ${:0.2f}".format(tot_cost))

main()