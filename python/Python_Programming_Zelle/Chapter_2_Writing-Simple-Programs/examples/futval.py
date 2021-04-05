#futval.py

def main():
    print("Finds the future value of a 10-year investment")
    principal = eval(input("Enter principal: "))
    apr = eval(input("Enter apr: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The future value is:",principal)

main()