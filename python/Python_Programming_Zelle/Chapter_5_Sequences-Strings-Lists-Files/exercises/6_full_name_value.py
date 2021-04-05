#full_name_value.py

def main():
    inputName = input("Enter a name: ")

    nameList = []
    nameVal = 0
    for name in inputName.split():
        for ch in name:
            print("{0}-{1}".format(ch,ord(ch.upper())-64))
            nameVal = nameVal + (ord(ch.upper()) - 64)

    print("{0}-{1}".format(inputName,nameVal))
main()