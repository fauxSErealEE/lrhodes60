#convert.py

def main():
    print("This program takes a temperature in Celsius and returns the temperature in Fahrenheit")

    celsius = eval(input("What is the degrees in Celsius temperature? "))
    fahrenheit = (1.8 * celsius) + 32
    for i in range(5):
        print("The temperature in Fahrenheit is", fahrenheit, "degress.")

main()