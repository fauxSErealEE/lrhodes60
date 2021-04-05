#calculator.py

def main():

    print("This program is an interactive calculator.")
    print("Enter the simple expression when prompted.")

    for i in range(100):
        output = eval(input("Enter simple expression: "))
        print(output)

main()