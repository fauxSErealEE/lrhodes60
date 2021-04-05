#draw_triangle.pyw

from graphics import *
import math as math

def draw_axis(win, xll, yll, xur, yur, numTicks):
    # Take in the GraphWin object to draw on, it's Coordinate system, 
    # and how many ticks to draw on the window
    # win = GraphWin object
    # xll = lower left x-axis
    # xur = upper right x-axis
    # numTicks = number of ticks on the axis
    
    yAxis = Line(Point((xur+xll)/2,yll),Point((xur+xll)/2,yur))
    yAxis.draw(win)
    xAxis = Line(Point(xll,(yur+yll)/2),Point(xur,(yur+yll)/2))
    xAxis.draw(win)
    for i in range(numTicks + 1):
        yTickOrig = Line(Point(xll, (yur+yll)-(yur-yll)/40),Point(xll,(yur+yll)+(yur-yll)/40)).draw(win)
        yTickCopy = yTickOrig.clone()
        yTickCopy.move(i * ((yur-yll) / numTicks), 0)
        yTickCopy.draw(win)
        xTickOrig = Line(Point(((xur+xll)-(xur-xll))/40,yll), Point((xur+xll)+(xur-xll)/40,yll)).draw(win)
        xTickCopy = xTickOrig.clone()
        xTickCopy.move(0, i * ((xur-xll)/ numTicks))
        xTickCopy.draw(win)

def main():
    xll = -10
    yll = -10
    xur = 10
    yur = 10
    win = GraphWin(width=500,height=500)
    win.setCoords(xll,yll,xur,yur)
    draw_axis(win, xll, yll, xur, yur, 20)
    prompt = Text(Point((xur+xll)/2,0.8*yur),"Click three points to draw the triangle").draw(win)

    #Get the two points
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    #Draw the shape then display some info
    drawShape = Polygon(p1,p2,p3).draw(win)
    drawShape.setFill("blue")
    draw_axis(win, xll, yll, xur, yur, 20)

    #define sides a, b ,c
    #a is p1 to p2
    #b is p2 to p3
    #c is p1 to p3

    dxA = abs(p1.getX() - p2.getX())
    dyA = abs(p1.getY() - p2.getY())
    dxB = abs(p2.getX() - p3.getX())
    dyB = abs(p2.getY() - p3.getY())
    dxC = abs(p1.getX() - p3.getX())
    dyC = abs(p1.getY() - p3.getY())

    a = math.sqrt(dxA**2 + dyA**2)
    b = math.sqrt(dxB**2 + dyB**2)
    c = math.sqrt(dxC**2 + dyC**2)

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c

    areaText = Text(Point((xur+xll)/2,0.7*yur),"Area: {:.2f}".format(area)).draw(win)
    perimeterText = Text(Point((xur+xll)/2,0.6*yur),"Perimeter: {:.2f}".format(perimeter)).draw(win)

    prompt.setText("Click to Close")
    win.getMouse()

main()