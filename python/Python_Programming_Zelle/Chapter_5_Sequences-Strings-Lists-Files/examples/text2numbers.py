#text2numbers.py

def main():
    print("This program converts a textual message into a squence")
    print("of numbers representing the Unicode encoding of the message.\n")

    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    for ch in message:
        print(ord(ch), end=" ")

    print()

main()