# Fashion Pattern - Python Code - Elizabeth Tweedale

from turtle import *
from random import randint

myArt = Turtle()
myArt.penup()
myArt.goto(-360,330)

r, g, b = 0, 0, 0
colormode(255)
#speed(0)

def chooseColor():
    global r,g,b
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    
    myArt.pencolor(r,g,b)
    myArt.fillcolor(r,g,b)
    
    print ("Color is:", r, g, b)

def drawSquare():
    myArt.begin_fill()
    myArt.pendown()
    for i in range(4):
        myArt.forward(50)
        myArt.right(90)
    myArt.penup()
    myArt.end_fill()

    print ("Square Drawn")

def drawRow():
    for i in range(10):
        chooseColor()
        drawSquare()
        myArt.forward(50)

# draw each row and move down
for j in range(10):
    drawRow()
    myArt.backward(500)
    myArt.right(90)
    myArt.forward(50)
    myArt.left(90)
