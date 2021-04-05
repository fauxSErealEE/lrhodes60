#convert.py

def main():
    print("This program takes a temperature in Fahrenheit and returns the temperature in Celsius ")

    F = eval(input("What is the degrees in Fahrenheit temperature? "))
    celsius = 5/9 * (F-32)
    print("The temperature in Celsius is", celsius, "degress.")

main()