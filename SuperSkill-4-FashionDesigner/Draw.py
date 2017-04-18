# Sketching Project - Python Code - Elizabeth Tweedale
# Based on Python 3 Included Examples

from tkinter import *           # imports the tkinter GUI module

myPen = "up"                    # create your pen 
myX, myY = None, None           # set the X and Y position to None

def main():                     # this is the main function of your program
    root = Tk()                 # initialise the canvas
    mySketch = Canvas(root)     # call your canvas mySketch
    mySketch.pack()
    mySketch.bind("<Motion>", motion)   # motion is your mouse movement
    mySketch.bind("<ButtonPress-1>", myPenDown) # myPenDown is when you are holding down the left mouse button 
    mySketch.bind("<ButtonRelease-1>", myPenUp) # myPenUp is when you release the left mouse button
    root.mainloop()             # starts the main event loop

def myPenDown(event):           # define what should happen when your pen is down
    global myPen
    myPen = "down"              # you only want to draw when the button is down
                                # because "<Motion>" events happen -all the time-

def myPenUp(event):             # define what should happen when your pen is up
    global myPen, xOld, yOld
    myPen = "up"
    myX = None                  # reset the line start when you let go of the button
    myY = None

def motion(event):              # define what to do when your mouse is in motion
    if myPen == "down":         # only draw if your pen is "down"
        global myX, myY
        if myX is not None and myY is not None:
            event.widget.create_line(myX,myY,event.x,event.y,smooth=TRUE)
                                # here's where you draw your sketch!
        myX = event.x
        myY = event.y

if __name__ == "__main__":      # now that all of your events are defined, start the mainloop!
    main()
