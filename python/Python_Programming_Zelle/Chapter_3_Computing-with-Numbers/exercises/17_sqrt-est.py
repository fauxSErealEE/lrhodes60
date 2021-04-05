#sqrt-est.py

import math

def main():
    x = eval(input("Enter number you want to square root: "))
    n = eval(input("How many guesses do I get? "))

    guess = x / 2
    for i in range(2,n+1,1):
        guess = float((guess + (x / guess)) / 2)

    err = guess - math.sqrt(x)
    print("The estimated value in",n,"guesses is",guess)
    print("The error is",err)
main()