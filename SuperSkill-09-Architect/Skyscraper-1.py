# Skyscraper Project - 1 - Button - Python Code - Elizabeth Tweedale
from tkinter import *

def newSkyscraper():                    # Try changing the following 5 numbers and then re-running your program to design your skyscraper!
    winW = 10                           # Set the number of windows wide
    winH = 15                           # Set the number of windows high
    w = 15                              # Set the width of the windows
    h = 20                              # Set the height of the windows
    gap = 2                             # Set the window gap

    # Draw main building
    myBuilding.create_rectangle(gap,gap,(winW+2)*gap+winW*w,(winH+2)*gap+winH*h,    # startX(left),starty(top),finishX(right),finishY(bottom)
                                        outline="gray", fill="gray")                # outline and fill colours
    # Draw windows
    for i in range(winW):
        for j in range(winH):
            myBuilding.create_rectangle(((w+gap)*i+2*gap),                          # startX(left)
                                        ((h+gap)*j+2*gap),                          # startY(top)
                                        ((w+gap)*i+(2*gap+w)),                      # finsihX(right)
                                        ((h+gap)*j+(2*gap+h)),                      # finishY(bottom)
                                        outline="black",fill="white")               # outline, fill colours
                                                                                    # Try using different colours such as "blue" or "red"
    myBuilding.pack(fill=BOTH, expand=1)                                            # Add ALL of the rectangles to your Canvas
    
""" Main Program """
root = Tk()                                                                         # Set up Tkinter
myBuilding = Canvas(root, width=500, height=500)                                    # Set up Canvas
root.title("Skyscraper")                                                            # Set the title of your screen
myBuilding.pack()                                                                   # Pack adds everything to the Tkinter Canvas

""" Draw Button """
button = Button(root, text="Draw Skyscraper", command=newSkyscraper)                # Create a button to draw the skyscraper
button.pack()                                                                       # Add it to the Canvas

root.mainloop()                                                                     # start the main loop
