#draw_squares.pyw

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50),Point(83,83))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newShape = shape.clone()
        newShape.move(dx,dy)
        newShape.draw(win)
    output = Text(Point(100,180),"Click to quit")
    output.draw(win)
    win.getMouse()
    win.close()
main()