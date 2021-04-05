#exam_score_chart.py

import os
from graphics import *

def main():
    infileName = input("Enter filename with scores: ")

    fpath = os.path.dirname(__file__)
    infilePath = fpath + "\\" + infileName
    infile = open(infilePath,"r")

    studentName = []
    studentScore = []

    for fileLine in infile:
        wordCount = 0
        for word in fileLine.split():
            if (wordCount == 0):
                studentName.append(word)
                wordCount = 1
            elif (wordCount == 1):
                studentScore.append(word)
                wordCount = 0
    numStudents = len(studentName)

    win = GraphWin("Exam Scores",500,500)
    win.setCoords(-40, -2, 110, 5*(numStudents+2))

    for n in range(0,110,10):
        label = Text(Point(n,5*(numStudents+1)),n).draw(win)
        labelLine = Line(Point(n,-1),Point(n,5*(numStudents+0.75))).draw(win)

    for i in range(0,numStudents,1):
        stuName = Text(Point(-20,5*(numStudents-i)),studentName[i])
        stuName.draw(win)
        stuScore = Rectangle(Point(0,5*(numStudents-i)-1),Point(studentScore[i],5*(numStudents-i)+1)).draw(win)
        if (eval(studentScore[i]) >= 90):
            stuScore.setFill('blue')
        elif (eval(studentScore[i]) >= 80):
            stuScore.setFill('green')
        elif (eval(studentScore[i]) >= 70):
            stuScore.setFill('yellow')
        elif (eval(studentScore[i]) >= 60):
            stuScore.setFill('orange')
        else:
            stuScore.setFill('red')

    win.getMouse()
main()