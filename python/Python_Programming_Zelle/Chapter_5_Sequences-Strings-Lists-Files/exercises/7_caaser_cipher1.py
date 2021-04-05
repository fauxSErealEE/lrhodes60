#caeser_cipher1.py

def main():
    loop = True
    while loop:
        select = eval(input("Are you encoding a message (1) or decoding a message (2)? "))
        if (select == 1) | (select == 2):
            loop = False

    inputCode = input("Enter text to be (de)ciphered: ")
    keyCode = eval(input("Enter key code: "))
    if (select == 2):
        keyCode = -keyCode

    outputCodeList = []
    for ch in inputCode:
        if (ord(ch) != 32):
            outputCodeList.append(chr(ord(ch) + keyCode))
        else:
            outputCodeList.append(ch) #perserve the space character
    outputCode = "".join(outputCodeList)
    print("The (de)ciphered text is: ",outputCode)
main()