#userfile.py
# Program to create a file of usernames in batch mode.

import os

def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    # get file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    #open the files
    fpath = os.path.dirname(__file__)
    infilePath = fpath + "\\" + infileName
    outfilePath = fpath + "\\" + outfileName
    infile = open(infilePath, "r")
    outfile = open(outfilePath, "w")

    #process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the user name
        uname = (first[0] + last[:7]).lower()
        # write it to the output file
        print(uname, file=outfile)

    #close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)
main()