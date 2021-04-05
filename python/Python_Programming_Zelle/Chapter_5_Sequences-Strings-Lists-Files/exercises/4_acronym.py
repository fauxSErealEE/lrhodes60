#acronym.py

def main():
    phrase = input("Enter any phrase: ")

    acronymList = []

    for word in phrase.split():
        acronymList.append(word[0].upper())

    acronym = "".join(acronymList)
    print("\nThe acronym is",acronym)
main()