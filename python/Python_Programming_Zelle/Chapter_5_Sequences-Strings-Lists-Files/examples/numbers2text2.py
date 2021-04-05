#numbers2text2.py

def main():
    inString = input("Please enter the Unicode-encoded message: ")

    chars = []
    for numStr in inString.split():
        codeNum = eval(numStr)
        chars.append(chr(codeNum))
        print(chars)
    
    message = "".join(chars)
    print("\nThe decoded message is:",message)
main()