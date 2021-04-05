#futval_graph.py

from graphics import *

def main():
    #Introduction
    print("This program plots the growth of a 10-year investment.")

    #Get initial principal and apr
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: ")) / 100
    

    #Create the graphics window
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75,-300,11.5,10400)
    Text(Point(-1,0),' 0.0K').draw(win)
    Text(Point(-1,2500),' 2.5K').draw(win)
    Text(Point(-1,5000),' 5.0K').draw(win)
    Text(Point(-1,7500),' 7.5K').draw(win)
    Text(Point(-1,10000),' 10.K').draw(win)

    #Draw initial principal bar
    bar = Rectangle(Point(0,00), Point(1,principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw successive years
    for year in range(1,11):
        #calc value for the next year
        principal = principal * (1 + apr)
        #draw bar for year
        bar = Rectangle(Point(year,0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()
main()