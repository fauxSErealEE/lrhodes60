#convert.py

def main():
    print("This program takes a temperature in Celsius and returns the temperature in Fahrenheit")
    print("")

    C = 0

    print("Celsius    Fahrenheit")
    print("---------------------")
    for i in range(11):
        F = 1.8 * C +32
        print("   ",C,"            ",F)
        C = C + 10

main()