#chemistry.pi

import math as math

def main():
    hyd = eval(input("Enter number of hydrogens: "))
    carb = eval(input("Enter number of carbons: "))
    oxy = eval(input("Enter number of oxygens: "))

    hyd_wgt = 1.0079
    carb_wgt = 12.001
    oxy_wgt = 15.9994

    tot_wgt = hyd * hyd_wgt + carb * carb_wgt + oxy * oxy_wgt

    print("The total molecular weight in grams per mole of your hydrocarbon is {:0.4f}".format(tot_wgt))

main()