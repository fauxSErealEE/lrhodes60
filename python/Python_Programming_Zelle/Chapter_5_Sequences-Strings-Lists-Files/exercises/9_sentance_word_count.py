#sentance_word_count.py

def main():
    inSentance = input("Type the sentance: ")

    wordCount = 0
    for word in inSentance.split():
        wordCount += 1
    print("The total word count is {0}".format(wordCount))
main()