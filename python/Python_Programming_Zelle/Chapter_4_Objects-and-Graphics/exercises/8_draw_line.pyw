#draw_line.pyw

from graphics import *
import math as math

def main():
    win = GraphWin(width=500,height=500)
    win.setCoords(-250, -250, 250, 250)
    prompt = Text(Point(0,200),"Click two points to draw a line").draw(win)

    #Get the two points
    p1 = win.getMouse()
    p2 = win.getMouse()

    #Draw the line then display some info
    drawLine = Line(p1,p2).draw(win)
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    if(dx == 0):
        slope = "undefined"
    else:
        slope = dy / dx
    length = math.sqrt(dx**2 + dy**2)

    slopeText = Text(Point(0,175),"Slope: {:.2f}".format(slope)).draw(win)
    lengthText = Text(Point(0,150),"Length: {:.2f}".format(length)).draw(win)

    prompt.setText("Click to Close")
    win.getMouse()

main()