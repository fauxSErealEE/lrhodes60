#avg_word_length.py

def main():
    inputSentance = input("Type sentence: ")

    totalChars = 0
    wordCount = 0
    for word in inputSentance.split():
        wordCount += 1
        totalChars += len(word)
    print("The average word length was {0:.2f} letters long".format(float(totalChars / wordCount)))
main()