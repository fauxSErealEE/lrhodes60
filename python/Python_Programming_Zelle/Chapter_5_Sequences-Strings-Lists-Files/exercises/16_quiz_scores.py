#quiz_scores.py

import os
from graphics import *
import random as random

def main():
    # infileName = input("Enter filename: ")
    infileName = "16_quiz_scores.txt"

    fpath = os.path.dirname(__file__)
    infilePath = fpath + "\\" + infileName
    infile = open(infilePath,"r")

    quizScoreHist = [0] * 11

    for line in infile:
        quizScore = eval(line)
        quizScoreHist[quizScore] += 1

    win = GraphWin("Quiz Scores",500,500)
    win.setCoords(-5, -1, 55, max(quizScoreHist)+1)

    for n in range(0,max(quizScoreHist)+1,1):
        Line(Point(0,n),Point(50,n)).draw(win)
        Text(Point(-2,n),n).draw(win)

    for i in range(0,55,5):
        label = Text(Point(i,-0.25),i // 5).draw(win)
        histBar = Rectangle(Point(i-1,0),Point(i+1,quizScoreHist[i//5])).draw(win)
        histBar.setFill(color_rgb(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))


    win.getMouse()
main()