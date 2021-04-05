#month.py

def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = eval(input("Enter a month number (1-12): "))
    while ( (n < 1) | (n > 12) ):
        n = eval(input("Out of range. Try again. Enter a month number (1-12): "))

    pos = (n-1) * 3

    monthAbbrev = months[pos:pos+3]

    print("The month abbreviation is",monthAbbrev + ".")

main()    