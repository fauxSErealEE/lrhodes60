#circle-line.py

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

    #get circle radius
    radius = eval(input("Enter Circle Radius (<=10): "))
    if (radius < 0):
        print("I assume you meant the positive version, I changed it for you")
        radius = radius * (-1)
    
    if (radius > 10):
        print("You didn't follow the directions. I clipped it at 10")
        radius = 10

    #get line y-intercept
    yIntercept = eval(input("Enter y-intercept [-10,10]: "))
    if (yIntercept < -10) | (yIntercept > 10):
        print("You suck at this. I'm choosing for you")
        print("Your y-intercept is -2")
        yIntercept = -2
    
    #Create window and draw axis
    win = GraphWin(width=500,height=500)
    win.setCoords(-10, -10, 10, 10)
    draw_axis(win, -10, -10, 10, 10, 20)
    
    #Draw the shapes
    drawCricle = Circle(Point(0,0),radius)
    drawCricle.setOutline("green")
    drawCricle.draw(win)
    drawLine = Line(Point(-10,yIntercept), Point(10,yIntercept))
    drawLine.setOutline("blue")
    drawLine.draw(win)

    #Find their intercept
    xNegRoot = -math.sqrt(radius**2 - yIntercept**2)
    xPosRoot = math.sqrt(radius**2 - yIntercept**2)
    xNegMark = Text(Point(xNegRoot,yIntercept), "X")
    xNegMark.setTextColor("red")
    xNegMark.setSize(18)
    xNegMark.draw(win)
    xPosMark = Text(Point(xPosRoot,yIntercept), "X")
    xPosMark.setTextColor("red")
    xPosMark.setSize(18)
    xPosMark.draw(win)

    #Print the intercept on there
    Text(Point(xNegRoot-1,yIntercept+1),"{:.3f}".format(xNegRoot)).draw(win)
    Text(Point(xPosRoot+1,yIntercept+1),"{:.3f}".format(xPosRoot)).draw(win)

    input("Press Enter to quit")
main()