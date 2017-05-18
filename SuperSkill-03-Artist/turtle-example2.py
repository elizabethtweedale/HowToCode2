# Turtle Art - 2 - Python Code - Elizabeht Tweedale

from turtle import *        # imports the turtle module

from random import randint  # from the random module import the function randint
                            # like turtle it is a module, but this time we are only
                            # reading in one function, not all of them with *
speed(0)                   
bgcolor('black')
      
x = 0
      
while x < 400:          # while the value of x is less than 120, continue

    # create variables for r,g,b colours
    r = randint(0,255)  # set the variable to a random integer between 0 and 255
    g = randint(0,255)  # note: these numbers will change every time the loop runs
    b = randint(0,255)

    colormode(255)      # this tells Python to accept 3 integers: r,g,b for colour   
    
    pencolor(r,g,b)     # change the colour of the pen to the r,g,b coordinates
      
    fd(50 + x)
    rt(105)             # TRY > changing this to rt(91)... or another number!
    
    x = x+1             # adds 1 to the value of x

exitonclick()           # when you click, turtle exits
