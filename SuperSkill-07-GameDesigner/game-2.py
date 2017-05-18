# PyGame Game - 2 - Python Code - Elizabeht Tweedale
import pygame
from random import randint

def newPosition():              # Define a funciton to return a new (x,y) positions     *** NEW DEFINITION ***
    randomX = randint(0,1000)   # Find a random integer between the left and right edge
    randomY = randint(0,625)    # Find a random integer between the top and bottom edge
    return (randomX, randomY)   # Return the random x and y coordinates

''' SET UP CODE HERE '''
pygame.init()                                               # Set up PyGame
myClock = pygame.time.Clock()                               # Set up Clock
pygame.time.set_timer(pygame.USEREVENT, 1000)               # Set up Timer              #** NEW LINE **#

myScreen = pygame.display.set_mode([1000, 625])             # Set up Screen
pygame.display.set_caption('Bug Collecting')                # Set up Caption            #**  UPDATE  **#

myBackground = pygame.image.load('circuits.png').convert()  # Load Background

myPlayer = pygame.image.load('robot.png').convert()         # Load Player
myPlayer.set_colorkey((0,0,0))

mySound = pygame.mixer.Sound('laser.ogg')                   # Load Sound

myFont = pygame.font.SysFont("monospace", 30)               # Load Font                 #** NEW LINE **#

myBug = newPosition()    # Create New Bug position                                      #** NEW LINE **#

playerX = 500           # Set Player's X position
playerY = 300           # Set Player's Y position

score = 0               # Set Score to 0                                                #** NEW LINE **#
time = 60               # Set Time to 60 seconds                                        #** NEW LINE **#
GOLD = (255,200,0)      # Define GOLD Colour                                            #** NEW LINE **#

done = False            # Main event loop:
while not done:
    ''' EVENT PROCESSING HERE '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and time > 0:                                 #**  UPDATE  **#
            if event.key == pygame.K_LEFT:
                playerX -= 20
            if event.key == pygame.K_RIGHT:
                playerX += 20
            if event.key == pygame.K_UP:
                playerY -= 20
            if event.key == pygame.K_DOWN:
                playerY += 20
        elif event.type == pygame.USEREVENT:                                            #** NEW LINE **#
            if time > 0:                                                                #** NEW LINE **#
                time -= 1                                                               #** NEW LINE **#

    ''' GAME LOGIC HERE '''
    # If the player position matches the bug position, collect it and add 1 to the score.
    if playerX <= (myBug[0]+30) and playerX >= (myBug[0]-30):                                   #**  UPDATE  **#
        if playerY <= (myBug[1]+50) and playerY >= (myBug[1]-50):                               #** NEW LINE **#
            mySound.play()                                          # Play Sound
            score += 1; print ('Score:',score)                      # Add 1 to the Score        #** NEW LINE **#
            myBug = newPosition()                                   # Create New Bug Position   #** NEW LINE **#

    myTextScore = myFont.render(("Score: " + str(score)), 1, GOLD)  # Update Score Text         #** NEW LINE **#
    myTextTime = myFont.render(("Time: " + str(time)), 1, GOLD)     # Update Time Text          #** NEW LINE **#

    ''' DRAWING CODE HERE '''
    myScreen.blit(myBackground,[0,0])                               # Draw Background
    myScreen.blit(myPlayer, [playerX-30, playerY-50])               # Draw Player
    pygame.draw.ellipse(myScreen,GOLD,(myBug[0],myBug[1],10,20))    # Draw Bug          #** NEW LINE **#
    myScreen.blit(myTextScore, (50, 50))                            # Draw Score        #** NEW LINE **#
    myScreen.blit(myTextTime, (50, 100))                            # Draw Time         #** NEW LINE **#

    myClock.tick(60)                                                # Tick Clock
    pygame.display.flip()                                           # Flip Display
    
pygame.quit()
