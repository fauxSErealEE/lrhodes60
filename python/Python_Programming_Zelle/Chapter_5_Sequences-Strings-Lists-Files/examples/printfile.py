#printfile.py

import os

def main():
    cwd = os.path.dirname(__file__)

    fname = input("Enter filename: ")
    fpath = cwd + "\\" + fname
    infile = open(fpath,"r")
    data = infile.read()
    print(data)

main()