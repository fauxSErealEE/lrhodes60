#draw_rectangle.pyw

from graphics import *

def main():
    win = GraphWin(width=500,height=500)
    win.setCoords(-250, -250, 250, 250)
    prompt = Text(Point(0,200),"Click two points to draw the opposite corners of a rectangle").draw(win)

    #Get the two points
    p1 = win.getMouse()
    p2 = win.getMouse()

    #Draw the shape then display some info
    drawShape = Rectangle(p1,p2).draw(win)
    length = abs(p2.getX() - p1.getX())
    height = abs(p2.getY() - p1.getY())

    area = length * height
    perimeter = (2 * length) + (2 * height)

    areaText = Text(Point(0,175),"Area: {:.2f}".format(area)).draw(win)
    perimeterText = Text(Point(0,150),"Perimeter: {:.2f}".format(perimeter)).draw(win)

    prompt.setText("Click to Close")
    win.getMouse()

main()