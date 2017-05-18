# Turtle Art - 1 - Python Code - Elizabeth Tweedale

from turtle import * # imports the turtle module
                     # * stands for all, which makes things easier

speed(0)            # sets the speed of drawing to 0, which is the fastest
pencolor('pink')    # sets the color of the pen/lines to white
bgcolor('black')    # sets the color of the background/canvas to black

x = 0               # creates a variable x with value 0

# move turtle over
penup()             # pick up the pen
lt(180)             # lt() means rotate left by a certain angle
fd(100)             # fd() means move forward - bk() means move back
rt(90)              # rt() means rotate right
pendown()           # place the pen back down for drawing


while x < 120:      # while the value of x is less than 120, continue
    
    fd(150)
    rt(62)
    fd(150)
    rt(62)
    fd(150)
    rt(62)
    fd(150)
    rt(62)
    fd(150)
    rt(62)
    fd(150)
    rt(62)

    rt(12.25)
    x = x+1         # adds 1 to the value of x

exitonclick()       # when you click, turtle exits
