#face.pyw

from graphics import *

def main():
    win = GraphWin("Face",500,500)
    
    #draw the head first
    head = Oval(Point(100,450),Point(400,50))
    head.setFill("yellow")
    head.draw(win)

    leftEye = Oval(Point(125,240),Point(240,190))
    leftEye.setFill(color_rgb(255,255,255))
    leftEye.setOutline("black")
    leftEye.draw(win)

    pupilCenter = leftEye.getCenter()
    pupilRadius = (leftEye.getP2().getY() - leftEye.getP1().getY()) / 2
    leftPupil = Circle(pupilCenter, pupilRadius)
    leftPupil.setFill("black")
    leftPupil.draw(win)

    rightEye = leftEye.clone()
    rightEyeCenter = 2 * (head.getCenter().getX() - leftEye.getCenter().getX())
    rightEye.move(rightEyeCenter,0)
    rightEye.draw(win)

    rightPupil = leftPupil.clone()
    rightPupil.move(rightEyeCenter,0)
    rightPupil.draw(win)

    nose = Polygon(Point(225,250),Point(275,250),Point(250,275))
    nose.setFill("black")
    nose.draw(win)

    mouth = Oval(Point(150,380),Point(350,305))
    mouth.setFill("white")
    mouth.setOutline("black")
    mouth.draw(win)

    Text(Point(250,485),"Click to Close").draw(win)
    win.getMouse()

main()