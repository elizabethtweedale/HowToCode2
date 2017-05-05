# Soundboard Lion with PyGame - Python Code - Elizabeth Tweedale

import pygame

pygame.init()                                               # initialise PyGame - setting it up

screen = pygame.display.set_mode([800, 600])                # set the screen size to 800 x 600 pixels - it should be the same size as your picture!
pygame.display.set_caption('Super Skills')                  # set the caption of your screen to anything you would like, ours is called 'Super Skills'

click_sound = pygame.mixer.Sound("whirl.ogg")               # label your sound and load in the file - you can call 'click_sound' anything you would like

background_position = [0, 0]                                # set the position of the background to start in the top left corner which is [0, 0]
background_image = pygame.image.load("lion.jpg").convert()  # label your image and load in the file - you can call 'background_image' anything you would like

soundboard = True                                           # this is a boolean (True/False) which tells our program to continue - it can also be named anything

while soundboard:
    for event in pygame.event.get():                        # this is the main drawing event loop of the program - it captures any events that will happen
        if event.type == pygame.QUIT:                       # if the user quits the program, tell the program to stop
            soundboard = False
        elif event.type == pygame.MOUSEBUTTONDOWN:          # if the user clicks the mouse...
            player_position = pygame.mouse.get_pos()        # find the position of the mouse
            x = player_position[0]                          # return the 'x' coordinate (left to right / horizontal axis)
            # y = player_position[1]                        # FYI - this is what we could use to return the 'y' coordinate
            if x < 400:                                     # if 'x' is on the left half of the picture
                click_sound.play()                          # play the sound loaded in
                print ('Left Side Click', x)                # print the position to the console (just as a test - we don't actually need this line of code)
            else:
                click_sound.stop()                          # else if 'x' is on the right half of the picture, stop the sound
                print ('Right Side Click', x)               # again, print the position as a test

    screen.blit(background_image, background_position)      # set the background image and tell it where its position is
    pygame.display.flip()                                   # flip the screen to draw the background

pygame.quit()
