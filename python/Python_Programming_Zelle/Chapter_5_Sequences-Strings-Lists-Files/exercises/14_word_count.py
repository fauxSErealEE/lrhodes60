#word_count.py

import os

def main():
    infileName = input("Enter file name: ")

    #create the full filepath
    fpath = os.path.dirname(__file__)
    infilePath = fpath + "\\" + infileName
    infile = open(infilePath, "r")

    numLines = 0
    numWords = 0
    numChars = 0
    for line in infile:
        numLines += 1
        for word in line.split():
            numWords += 1
            numChars += len(word)
    
    print("Here are the stats the file {0}".format(infileName))
    print("\tNumber of lines: {0}\n\tNumber of words: {1}\n\tNumber of Characters: {2}"
            .format(numLines,numWords,numChars))
main()
