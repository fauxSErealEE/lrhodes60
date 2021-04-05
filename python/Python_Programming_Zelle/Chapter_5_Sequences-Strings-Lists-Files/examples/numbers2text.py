#numbers2text.py

def main():
    inString = input("Please enter the Unicode-encoded message: ")

    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)
        message = message + chr(codeNum)

    print("The decoded message is: ", message)
main()