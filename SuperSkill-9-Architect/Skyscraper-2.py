# Skyscraper Project - 2- Scales + Button - Python Code - Elizabeth Tweedale
from tkinter import *

def newSkyscraper():
    winW = scaleWinW.get()                                                          # Get the number of windows wide from the scale
    winH = scaleWinH.get()                                                          # Get the number of windows high from the scale
    w = scaleW.get()                                                                # Get the width of the windows from the scale
    h = scaleH.get()                                                                # Get the height of the windows from the scale
    gap = scaleGap.get()                                                            # Get the window gap from the scale
    
    myBuilding.delete("all")                                                        # This will clear the drawing before drawing new squares

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

""" Draw Scales """
scaleWinW = Scale(root, from_=5, to=30, orient=HORIZONTAL, label= "Windows Wide")   # Create a scale for the number of windows wide
scaleWinW.pack()                                                                    # Add it to the Canvas
# HINT - you can copy the above two lines for the next 4 scales and simply change the variable names - think of it like "SPOT THE DIFFERENCE"
scaleWinH = Scale(root, from_=5, to=30, orient=HORIZONTAL, label= "Windows High")   # Create a scale for the number of windows high
scaleWinH.pack()                                                                    # Add it to the Canvas

scaleW = Scale(root, from_=5, to=30, orient=HORIZONTAL, label= "Window Width")      # Create a scale for the windows' width
scaleW.pack()                                                                       # Add it to the Canvas

scaleH = Scale(root, from_=5, to=30, orient=HORIZONTAL, label= "Window Height")     # Create a scale for the windows' height
scaleH.pack()                                                                       # Add it to the Canvas

scaleGap = Scale(root, from_=2, to=20, orient=HORIZONTAL, label= "Window Gap")      # Create a scale for the size of the gap between windows...
scaleGap.pack()                                                                     # Did you notice the smaller numbers for the from_ and to?

""" Draw Button """
button = Button(root, text="Draw Skyscraper", command=newSkyscraper)                # Create a button to draw the skyscraper
button.pack()                                                                       # Add it to the Canvas

root.mainloop()                                                                     # start the main loop
