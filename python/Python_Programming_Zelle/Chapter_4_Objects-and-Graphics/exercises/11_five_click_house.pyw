#five_click_house.pyw

from graphics import *

def main():
    win = GraphWin("Draw a House",width=500,height=500)
    xll = 0
    yll = 0
    xur = 500
    yur = 500
    win.setCoords(xll, yll, xur, yur)

    prompt = Text( Point( (xur+xll)/2, 0.8*yur), "Get ready to draw a house. Click to begin").draw(win)
    win.getMouse()

    #Get and draw the house
    prompt.setText("Click for lower left corner of your house")
    houseLL = win.getMouse()
    prompt.setText("Click for upper right corner of your house")
    houseUR = win.getMouse()
    house = Rectangle(houseLL, houseUR).draw(win)

    #Get and draw the door
    prompt.setText("Click for upper middle of the door")
    doorUM = win.getMouse()
    doorWidth = ((houseUR.getX() - houseLL.getX()) / 5.0) #door is 1/5 of house width
    doorLL = Point(doorUM.getX() - (doorWidth/2.0), houseLL.getY())
    doorUR = Point(doorUM.getX() + (doorWidth/2.0), doorUM.getY())
    door = Rectangle(doorLL, doorUR).draw(win)

    #Get and draw the window
    prompt.setText("Click for center of the single window")
    windowCenter = win.getMouse()
    windowWidth = doorWidth / 2.0
    windowLL = Point(windowCenter.getX() - (windowWidth / 2.0), windowCenter.getY() - (windowWidth / 2.0))
    windowUR = Point(windowCenter.getX() + (windowWidth / 2.0), windowCenter.getY() + (windowWidth / 2.0))
    window = Rectangle(windowLL, windowUR).draw(win)

    #Get and draw the roof
    prompt.setText("Click for the peak of the roof")
    roofPeak = win.getMouse()
    roofLL = Point(houseLL.getX(), houseUR.getY())
    roofLR = Point(houseUR.getX(), houseUR.getY())
    roof = Polygon(roofLL, roofLR, roofPeak).draw(win)

    prompt.setText("Congratulations on your house! Click again to close")
    win.getMouse()   

main()