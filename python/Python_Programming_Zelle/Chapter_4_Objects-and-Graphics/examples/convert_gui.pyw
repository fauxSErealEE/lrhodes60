#convert_gui.pyw

from graphics import *
from buttonClick import *

def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    #Draw the interface
    Text(Point(1,3), "   Celsius Temperature:").draw(win)
    Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
    input = Entry(Point(2,3),5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.0),"Convert it")
    button.draw(win)
    rectLL = Point(1,1.5)
    rectUR = Point(2,2.5)
    rect = Rectangle(rectLL, rectUR)
    rect.draw(win)

    #wait for click inside button
    convertClick = False
    quitClick = False
    currClick = win.getMouse()
    rectButtonClick( rectButton=rect,buttonClick=currClick,window=win )

    #convert input
    celsius = eval(input.getText())
    fah = 9.0/5.0 * celsius + 32

    #display output and change button
    output.setText(fah)
    button.setText("Quit")

    #click the button to close the window
    currClick = win.getMouse()
    rectButtonClick( rectButton=rect,buttonClick=currClick,window=win )
    win.close()

    convertClick = True

main()