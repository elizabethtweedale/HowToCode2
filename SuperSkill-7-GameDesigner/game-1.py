# PyGame Game - 1 - Python Code - Elizabeht Tweedale
import pygame

''' SET UP CODE HERE '''
pygame.init()                                               # Set up PyGame
myClock = pygame.time.Clock()                               # Start Clock

myScreen = pygame.display.set_mode([1000, 625])             # Set up Screen
pygame.display.set_caption('Robot Bounce')                  # Set up Caption

myBackground = pygame.image.load('circuits.png').convert()  # Load Background

myPlayer = pygame.image.load('robot.png').convert()         # Load Player
myPlayer.set_colorkey((0,0,0))                              

mySound = pygame.mixer.Sound('laser.ogg')                   # Load Sound

playerX = 500           # Set Player's X position
playerY = 300           # Set Player's Y position

done = False            # Main event loop:
while not done:
    ''' EVENT PROCESSING HERE '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= 20
            if event.key == pygame.K_RIGHT:
                playerX += 20
            if event.key == pygame.K_UP:
                playerY -= 20
            if event.key == pygame.K_DOWN:
                playerY += 20

    ''' GAME LOGIC HERE '''
    # If the player is at the edge of the screen, then play a sound.
    if playerX <= 0 or playerX >= 1000 or playerY <= 0 or playerY >= 625:
            mySound.play()                              # Play Sound

    ''' DRAWING CODE HERE '''
    myScreen.blit(myBackground,[0,0])                   # Draw Background
    myScreen.blit(myPlayer, [playerX-30, playerY-50])   # Draw Player
   
    myClock.tick(60)                                    # Tick Clock
    pygame.display.flip()                               # Flip Display
    
pygame.quit()
