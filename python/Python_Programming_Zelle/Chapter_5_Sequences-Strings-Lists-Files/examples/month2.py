#month2.py

def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    n = eval(input("Enter a month number (1-12): "))
    while ( (n < 1) | (n > 12) ):
        n = eval(input("Out of range. Try again. Enter a month number (1-12): "))
    
    print("The month abbreviation is", months[n-1] + ".")
main()