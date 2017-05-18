# Simple Sound 2 with PyGame - Python Code - Elizabeth Tweedale

import pygame                                       # import PyGame - load all of the pygame resources

pygame.init()                                       # initialise PyGame - setting it up

screen = pygame.display.set_mode([400, 400])        # set the screen size to 400 x 400 pixels - try changing these numbers and see how it updates

pygame.display.set_caption('Super Skills')          # set the caption of your screen to anything you would like, ours is called 'Super Skills'

click_sound = pygame.mixer.Sound("whirl.ogg")       # label your sound and load in the file - you can call 'click_sound' anything you would like
key_sound = pygame.mixer.Sound("blip.ogg")      # NEW LINE! - lable and load another sound for pressing any key

soundboard = True                                   # this is a boolean (True/False) which tells our program to continue - it can also be named anything

while soundboard:                                   
    for event in pygame.event.get():                # this is the main drawing event loop of the program - it captures any events that will happen
        if event.type == pygame.QUIT:               # if the user quits the program, tell the program to stop
            soundboard = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks the mouse...
            click_sound.play()                      # play the sound loaded in
        elif event.type == pygame.KEYDOWN:      # NEW LINE! - if the user presses any key
            key_sound.play()                    # NEW LINE! - play the sound loaded in for pressing any key

print ("Goodbye Soundboard!")                       # print to the IDLE screen when you exit

pygame.quit()                                       # quit pygame
