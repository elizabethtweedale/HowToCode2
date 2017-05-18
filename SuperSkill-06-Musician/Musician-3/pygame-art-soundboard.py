# Art Soundboard with PyGame - Python Code - Elizabeth Tweedale

import pygame
pygame.init()

screen = pygame.display.set_mode([800, 500])
pygame.display.set_caption('Super Skills Art Soundboard')

top_left_sound = pygame.mixer.Sound("whirl.ogg")
bottom_left_sound = pygame.mixer.Sound("blip.ogg")
top_right_sound = pygame.mixer.Sound("charm.ogg")
bottom_right_sound = pygame.mixer.Sound("sleep.ogg")

background_position = [0, 0]
background_image = pygame.image.load("art.jpg").convert()

soundboard_end = False                                      # notice how this is the oposite of what we've done before

while not soundboard_end:                                   # now we are saying while it is NOT the end... 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            soundboard_end = True                           # and instead of changing True to False, we are changing False to True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player_position = pygame.mouse.get_pos()
            x = player_position[0]                          # this gives us the 'x' position of the mouse click
            y = player_position[1]                          # this gives us the 'y' position of the mouse click
            if x < 400:     # left side
                if y < 250:     # top
                    top_left_sound.play()                   # play the top left sound
                    print ('Top Left Click', x , y)
                else:           # bottom
                    bottom_left_sound.play()                # play the bottom left sound
                    print ('Bottom Left Click', x , y)
            else:           # right side
                if y < 250:     # top
                    top_right_sound.play()                  # play the top right sound
                    print ('Top Right Click', x , y)
                else:           # bottom
                    bottom_right_sound.play()               # play the bottom right sound
                    print ('Bottom Right Click', x , y)

    screen.blit(background_image, background_position)
    pygame.display.flip()

pygame.quit()
