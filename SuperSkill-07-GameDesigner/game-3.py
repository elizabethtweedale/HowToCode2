# PyGame Game - 3 - Python Code - Elizabeht Tweedale
import pygame
from random import randint

def newPosition():              # Define a funciton to create new random positions
    randomX = randint(10,990)   # Find a random integer between the left and right edge
    randomY = randint(10,615)   # Find a random integer between the top and bottom edge
    return (randomX, randomY)   # Return the x and y coordinates for the coin

def followPlayer(e,p,s):        # e = enemy position, p = player position, s = speed *** NEW DEFINITION ***
    x,y = e[0],e[1]
    if e[0] < p [0]:
        x = (e[0] + s)
    else: x = (e[0] - s)
    if e[1] < p [1]:
        y = (e[1] + s)
    else: y = (e[1] - s)
    return (x, y)

''' SET UP CODE HERE '''
pygame.init()                                               # Set up PyGame
myClock = pygame.time.Clock()                               # Set up Clock
pygame.time.set_timer(pygame.USEREVENT, 1000)               # Set up Timer

myScreen = pygame.display.set_mode([1000, 625])             # Set up Screen
pygame.display.set_caption('Bug Collecting')                # Set up Caption

myBackground = pygame.image.load('circuits.png').convert()  # Load Background

myPlayer = pygame.image.load('robot.png').convert()         # Load Player
myPlayer.set_colorkey((0,0,0))
myEnemy = pygame.image.load('enemy.png').convert()          # Load Enemy            #** NEW LINE **#
myEnemy.set_colorkey((0,0,0))                                                       #** NEW LINE **#

mySound = pygame.mixer.Sound('laser.ogg')                   # Load Sound

myFont = pygame.font.SysFont("monospace", 30)               # Load Font

myBug = newPosition()    # Create New Bug position
enemyPos = newPosition() # Create New Enemy position                                #** NEW LINE **#

playerX = 500            # Set Player's X position
playerY = 300            # Set Player's Y position

score = 0                # Set Score to 0
time = 60                # Set Time to 60 seconds
GOLD = (255,200,0)       # Define GOLD Colour

done = False             # Main event loop:
while not done:
    ''' EVENT PROCESSING HERE '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and time > 0:
            if event.key == pygame.K_LEFT:
                playerX -= 30
            if event.key == pygame.K_RIGHT:
                playerX += 30
            if event.key == pygame.K_UP:
                playerY -= 30
            if event.key == pygame.K_DOWN:
                playerY += 30
        elif event.type == pygame.USEREVENT:
            if time > 0:
                time -= 1
                if time%5 == 0: # Move the enimy every 5 seconds                        #** NEW LINE **#
                    enemyPos = newPosition()                                            #** NEW LINE **#

    ''' GAME LOGIC HERE '''
    # If the player position matches the bug position, collect it and add 1 to the score.
    if playerX <= (myBug[0]+30) and playerX >= (myBug[0]-30):
        if playerY <= (myBug[1]+50) and playerY >= (myBug[1]-50):
            mySound.play()                                          # Play Sound
            score += 1; print ('Score:',score)                      # Add 1 to the Score
            myBug = newPosition()                                   # Create New Bug Position

    # If the player position matches the enemy position, set time to 0 for GAME OVER.
    if playerX <= (enemyPos[0]+60) and playerX >= (enemyPos[0]-60):                     #** NEW LINE **#
        if playerY <= (enemyPos[1]+100) and playerY >= (enemyPos[1]-100):               #** NEW LINE **#
            time = 0                                                                    #** NEW LINE **#

    # If time is not 0, the enimy follows the player
    if time > 0:                                                                        #** NEW LINE **#
        enemyPos = followPlayer(enemyPos,(playerX,playerY),3)                           #** NEW LINE **#

    myTextScore = myFont.render(("Score: " + str(score)), 1, GOLD)  # Update Score Text
    myTextTime = myFont.render(("Time: " + str(time)), 1, GOLD)     # Update Time Text   

    ''' DRAWING CODE HERE '''
    myScreen.blit(myBackground,[0,0])                               # Draw Background
    myScreen.blit(myPlayer, [playerX-30, playerY-50])               # Draw Player
    myScreen.blit(myEnemy, [enemyPos[0]-30, enemyPos[1]-50])        # Draw Enemy        *** NEW LINE ***
    pygame.draw.ellipse(myScreen,GOLD,(myBug[0],myBug[1],10,20))    # Draw Bug
    myScreen.blit(myTextScore, (50, 50))                            # Draw Score
    myScreen.blit(myTextTime, (50, 100))                            # Draw Time

    # If time is 0, print GAME OVER
    if time == 0:                                                                       #** NEW LINE **#
        myScreen.blit(myFont.render("GAME OVER",1,GOLD), (50, 150))                     #** NEW LINE **#

    myClock.tick(60)                                                # Tick Clock
    pygame.display.flip()                                           # Flip Display
    
pygame.quit()
