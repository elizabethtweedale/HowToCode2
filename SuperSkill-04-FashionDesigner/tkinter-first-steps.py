# First Tkinter Project - Python Code - Elizabeth Tweedale

from tkinter import *                               # import the tkinter GUI module

def main():                                         # this is the main function of your program
    root = Tk()                                     # initialise tkinter root
    myWindow = Canvas(root, width=100, height=100)  # name your canvas myWindow and set the size to 100 x 100
    myWindow.pack()
    myWindow.bind("<Button-1>", testClick)          # this is where you will bind <Button-1> to a new event handler called testClick
    root.mainloop()                                 # starts the main event loop

def testClick(event):                               # define the testClick event handler and what to do when it occurs
    print ("Clicked at:", event.x, event.y)
    
main()                                              # start the mainloop by calling the main() function!
