# Sketching Project - Python Code - Elizabeth Tweedale
# Based on Python's Included Examples - you can find more in your Python Install program file!

from tkinter import *                           # import the tkinter GUI module

myPen = "up"                                    # create your pen 
myX, myY = None, None                           # set the X and Y position to None

def main():                                     
    root = Tk()                                 # initialise tkinter root
    mySketch = Canvas(root)                     # name your canvas mySketch; Can you remember how to set the size of the canvas to 600 x 600?
    mySketch.pack()
    mySketch.bind("<Motion>", motion)               # motion is your mouse movement
    mySketch.bind("<ButtonPress-1>", myPenDown)     # myPenDown is when you hold down the left mouse button 
    mySketch.bind("<ButtonRelease-1>", myPenUp)     # myPenUp is when you release the left mouse button
    root.mainloop()                                 # starts the main event loop

def myPenDown(event):                               # define what should happen when your pen is down
    global myPen                                    # tells the myPenDown definition that we will be using the myPen variable
    myPen = "down"                                  # you only want to draw when the button is down
                                                    # because the "<Motion>" events happen -all the time- 
def myPenUp(event):                                 # define what should happen when your pen is up
    global myPen, myX, myY                          # tells the myPenUp definition that we will be using these variables
    myPen = "up"                                    # you don't want to draw when the button is up
    myX = None                                      # reset the line start when you let go of the button
    myY = None

def motion(event):                                  # define what to do when your mouse is in motion
    global myX, myY
    if myPen == "down":                             # only draw if your pen is "down"
        if myX is not None and myY is not None:     # here's where you draw your sketch!
            event.widget.create_line(myX,myY,event.x,event.y,smooth=TRUE)
        myX = event.x
        myY = event.y

main()                                              # now that all of your events are defined, call main() to start the program
