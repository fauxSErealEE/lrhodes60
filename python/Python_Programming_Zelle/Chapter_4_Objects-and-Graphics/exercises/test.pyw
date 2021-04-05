from graphics import *

def main():
    win = GraphWin()
    win.setCoords(0,0,11,11)

    Text(Point(5,5),"Test").GraphWin(self,['left']).draw(win)
    Text(Point(5,5),"Test").draw(win)
    Text(Point(5,5),"Test").draw(win)

    win.getMouse()
main()