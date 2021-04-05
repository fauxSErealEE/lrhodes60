#buttonClick.py

from graphics import *

def rectButtonClick( rectButton, buttonClick, window ):
    buttonInside = False
    rectLL = rectButton.getP1()
    rectUR = rectButton.getP2()
    while (buttonInside==False):
        #keep checking until they get it right

        if ( (buttonClick.getX() >= rectLL.getX()) & (buttonClick.getX() <= rectUR.getX()) ):
            #check the button click for the x-coor

            if ( (buttonClick.getY() >= rectLL.getY()) & (buttonClick.getY() <= rectUR.getY()) ):
                #check the button click for the y-coor
                #if both good then do the thing, else don't
                buttonInside = True

        if (buttonInside==False):
            #get another click if the last one didn't work
            buttonClick = window.getMouse()

    #return that they clicked the button, not outside of it
    return buttonInside