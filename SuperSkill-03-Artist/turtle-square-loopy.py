# Turtle Loop - Python Code - Elizabeth Tweedale

import turtle               # imports the turtle module

loopy = turtle.Turtle()     # name your turtle 'loopy'

# use a for loop to repeat the forward/right code 4 times
for i in range(4):
    loopy.forward(50)
    loopy.right(90)
    
turtle.done()               # turtle is done
