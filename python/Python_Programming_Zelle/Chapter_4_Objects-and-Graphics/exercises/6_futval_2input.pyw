#futval_2input.pyw

from graphics import *
from buttonClick import *


def main():
    #Create the graphics window
    win = GraphWin("Investment Growth Chart", 320, 500)
    win.setBackground("white")
    win.setCoords(-1.75,-4000,11.5,10400)
    Text(Point(-1,0),' 0.0K').draw(win)
    Text(Point(-1,2500),' 2.5K').draw(win)
    Text(Point(-1,5000),' 5.0K').draw(win)
    Text(Point(-1,7500),' 7.5K').draw(win)
    Text(Point(-1,10000),' 10.K').draw(win)

    #Principal and apr inputs
    Text(Point(1,-1000),"Princial:").draw(win)
    principal = Entry(Point(4,-1000),7)
    principal.setText("0.0")
    principal.draw(win)
    Text(Point(2,-3000),"APR:").draw(win)
    apr = Entry(Point(4,-3000),3)
    apr.setText("0")
    apr.draw(win)

    #Make a button
    rect = Rectangle(Point(6,-3000),Point(11,-1000))
    rect.draw(win)
    Text(rect.getCenter(),"Create Graph").draw(win)

    #Check for the draw click
    currClick = win.getMouse()
    rectButtonClick( rectButton=rect,buttonClick=currClick,window=win )

    #After click, graph the principal and apr
    principalVal = eval(principal.getText())
    aprVal  = eval(apr.getText()) / 100

    # Draw initial principal bar
    bar = Rectangle(Point(0,00), Point(1,principalVal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw successive years
    for year in range(1,11):
        #calc value for the next year
        principalVal = principalVal * (1 + aprVal)
        #draw bar for year
        bar = Rectangle(Point(year,0), Point(year+1, principalVal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    Text(Point(4.5,9500),"Click to Close").draw(win)
    win.getMouse()
    win.close()
main()