import pygame, sys
import asyncio
from pygame.locals import *


async def main():
    #defining the colors with RGB tuples
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    CUSTOM = (255, 125, 0)

#defining direction of movement of the boxes and setting movespeed
    DOWNLEFT  = 'downleft'
    DOWNRIGHT = 'downright'
    UPLEFT    = 'upleft'
    UPRIGHT   = 'upright'
    MOVESPEED = 4

    pygame.init()

#setting window height and width to use for collision
    WINDOWHEIGHT = 800
    WINDOWWIDTH = 800
    windowSize = (WINDOWWIDTH, WINDOWHEIGHT)

#declaration of the window
    windowSize = (800, 800)
    windowSurface = pygame.display.set_mode(windowSize)
    pygame.display.set_caption('Animation')

    windowSurface.fill(CUSTOM)


#setting up the location where we place objects on the window.
    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('Hello world!', True, WHITE, BLUE)

    textRect = text.get_rect()

#declaring a variable for the central location of the window
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery

    windowSurface.blit(text, textRect)

#declaring a few boxes and setting their direction of movement
    b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
    b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}        
    b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT} 
    boxes = [b1, b2, b3]


#while loop to wait for the quit event and update box position
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #keep background color and shapes don't leave a line
        windowSurface.fill(CUSTOM)
        #move the boxes
        for b in boxes:
            if b['dir'] == DOWNLEFT:
                b['rect'].left -= MOVESPEED
                b['rect'].top += MOVESPEED
            if b['dir'] == DOWNRIGHT:
                b['rect'].left += MOVESPEED
                b['rect'].top += MOVESPEED
            if b['dir'] == UPLEFT:
                b['rect'].left -= MOVESPEED
                b['rect'].top -= MOVESPEED
            if b['dir'] == UPRIGHT:
                b['rect'].left += MOVESPEED
                b['rect'].top -= MOVESPEED

            #determining box collision when in contact with window edge
            if b['rect'].top < 0:
                # The box has moved past the top.
                if b['dir'] == UPLEFT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPRIGHT:
                    b['dir'] = DOWNRIGHT
            if b['rect'].bottom > WINDOWHEIGHT:
                # The box has moved past the bottom.
                if b['dir'] == DOWNLEFT:
                    b['dir'] = UPLEFT
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = UPRIGHT
            if b['rect'].left < 0:
                # The box has moved past the left side.
                if b['dir'] == DOWNLEFT:
                    b['dir'] = DOWNRIGHT
                if b['dir'] == UPLEFT:
                    b['dir'] = UPRIGHT        
            if b['rect'].right > WINDOWWIDTH:
                # The box has moved past the right side.
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPRIGHT:
                    b['dir'] = UPLEFT
            
            
            #printing the collision with the top of box 2 

            intersectionb1_2a = b1['rect'].clipline(b2['rect'].topleft,b2['rect'].topright)
            if intersectionb1_2a:
                if b1['dir'] == DOWNRIGHT:
                    b1['dir'] = UPRIGHT
                if b1['dir'] == DOWNLEFT:
                    b1['dir'] = UPLEFT
                if b2['dir'] == UPLEFT:
                    b2['dir'] = DOWNLEFT
                if b2['dir'] == UPRIGHT:
                    b2['dir'] = DOWNRIGHT
                print('collision 1-2 detected')

        #collision between box 1 and the bottom of box 2
            intersectionb1_2b = b1['rect'].clipline(b2['rect'].bottomleft,b2['rect'].bottomright)
            if intersectionb1_2b:
                if b1['dir'] == UPRIGHT:
                    b1['dir'] = DOWNRIGHT
                if b1['dir'] == UPLEFT:
                    b1['dir'] = DOWNLEFT
                if b2['dir'] == DOWNLEFT:
                    b2['dir'] = UPLEFT
                if b2['dir'] == DOWNRIGHT:
                    b2['dir'] = UPRIGHT
              

        #collision between box 1 and the right side of box 2
            intersectionb1_2c = b1['rect'].clipline(b2['rect'].topright,b2['rect'].bottomright)
            if intersectionb1_2c:
                if b1['dir'] == UPLEFT:
                    b1['dir'] = UPRIGHT
                if b1['dir'] == DOWNLEFT:
                    b1['dir'] = DOWNRIGHT
                if b2['dir'] == UPRIGHT:
                    b2['dir'] = UPLEFT
                if b2['dir'] == DOWNRIGHT:
                    b2['dir'] = DOWNLEFT
                

        #collision between box 1 and the left side of box 2
            intersectionb1_2d = b1['rect'].clipline(b2['rect'].topleft,b2['rect'].bottomleft)
            if intersectionb1_2d:
                if b1['dir'] == UPRIGHT:
                    b1['dir'] = UPLEFT
                if b1['dir'] == DOWNRIGHT:
                    b1['dir'] = DOWNLEFT
                if b2['dir'] == UPLEFT:
                    b2['dir'] = UPRIGHT
                if b2['dir'] == DOWNLEFT:
                    b2['dir'] = DOWNRIGHT
                print('collision 1-2 detected')

   

   #COLLISION BETWEEN BOX 1 AND BOX 3

            intersectionb1_3a = b1['rect'].clipline(b3['rect'].topleft,b3['rect'].topright)
            if intersectionb1_3a:
                if b1['dir'] == DOWNRIGHT:
                    b1['dir'] = UPRIGHT
                if b1['dir'] == DOWNLEFT:
                    b1['dir'] = UPLEFT
                if b3['dir'] == UPLEFT:
                    b3['dir'] = DOWNLEFT
                if b3['dir'] == UPRIGHT:
                    b3['dir'] = DOWNRIGHT

        #collision between box 1 and the bottom of box 3
            intersectionb1_3b = b1['rect'].clipline(b3['rect'].bottomleft,b3['rect'].bottomright)
            if intersectionb1_3b:
                if b1['dir'] == UPRIGHT:
                    b1['dir'] = DOWNRIGHT
                if b1['dir'] == UPLEFT:
                    b1['dir'] = DOWNLEFT
                if b3['dir'] == DOWNLEFT:
                    b3['dir'] = UPLEFT
                if b3['dir'] == DOWNRIGHT:
                    b3['dir'] = UPRIGHT
              

        #collision between box 1 and the right side of box 3
            intersectionb1_3c = b1['rect'].clipline(b3['rect'].topright,b3['rect'].bottomright)
            if intersectionb1_3c:
                if b1['dir'] == UPLEFT:
                    b1['dir'] = UPRIGHT
                    print('upleft collide')
                if b1['dir'] == DOWNLEFT:
                    b1['dir'] = DOWNRIGHT
                if b3['dir'] == UPRIGHT:
                    b3['dir'] = UPLEFT
                if b3['dir'] == DOWNRIGHT:
                    b3['dir'] = DOWNLEFT
                

        #collision between box 1 and the left side of box 2
            intersectionb1_3d = b1['rect'].clipline(b3['rect'].topleft,b3['rect'].bottomleft)
            if intersectionb1_3d:
                if b1['dir'] == UPRIGHT:
                    b1['dir'] = UPLEFT
                if b1['dir'] == DOWNRIGHT:
                    b1['dir'] = DOWNLEFT
                if b3['dir'] == UPLEFT:
                    b3['dir'] = UPRIGHT
                if b3['dir'] == DOWNLEFT:
                    b3['dir'] = DOWNRIGHT


            pygame.draw.rect(windowSurface, b['color'], b['rect'])

        pygame.display.update()
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())