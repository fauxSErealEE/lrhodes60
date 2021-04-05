# draw_axis.py

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