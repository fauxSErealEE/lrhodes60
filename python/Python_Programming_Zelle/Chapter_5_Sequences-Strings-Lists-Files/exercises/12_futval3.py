#futval3.py

def main():
    print("Finds the future value of a 10-year investment")
    principal = eval(input("Enter principal: "))
    apr = eval(input("Enter apr: "))
    yrs = eval(input("Enter numbers of years: "))

    print("{0:5} {1:9}".format('Year'.center(9),'Value'.center(9)))
    print("------------------")
    for i in range(0,yrs+1,1):
        print("{0:5} ${1:.2f}".format(str(i).center(9),principal))
        principal = principal * (1 + apr)
main()