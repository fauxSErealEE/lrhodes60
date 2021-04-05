#convert.py

def main():
    celsius = eval(input("What is the degrees in Celsius temperature? "))
    fahrenheit = (1.8 * celsius) + 32
    print("The temperature in Fahrenheit is", fahrenheit, "degress.")

main()