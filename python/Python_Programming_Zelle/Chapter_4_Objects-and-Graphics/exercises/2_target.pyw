#target.pyw

from graphics import *

def main():
    win = GraphWin("Archery Target",500,500)
    win.setCoords(0,0,14,14)

    whiteCirc = Circle(Point(7,7), 5)
    whiteCirc.setFill("white")
    whiteCirc.setOutline("black")
    whiteCirc.draw(win)

    blackCirc = Circle(Point(7,7), 4)
    blackCirc.setFill("black")
    blackCirc.setOutline("black")
    blackCirc.draw(win)

    blueCirc = Circle(Point(7,7), 3)
    blueCirc.setFill("blue")
    blueCirc.setOutline("black")
    blueCirc.draw(win)

    redCirc = Circle(Point(7,7), 2)
    redCirc.setFill("red")
    redCirc.setOutline("black")
    redCirc.draw(win)

    yellowCirc = Circle(Point(7,7), 1)
    yellowCirc.setFill("yellow")
    yellowCirc.setOutline("black")
    yellowCirc.draw(win)

    win.getMouse()
    win.close()
main()