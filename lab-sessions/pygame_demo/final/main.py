import pygame, sys
import asyncio
from pygame.locals import *

async def main():
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    CUSTOM  = (  255,   125, 125)

    DOWNLEFT  = 'downleft'
    DOWNRIGHT = 'downright'
    UPLEFT    = 'upleft'
    UPRIGHT   = 'upright'

    MOVESPEED = 4

    # boxes definition
    b1 = {'rect':pygame.Rect(300, 80, 50, 100),
        'color':RED, 'dir':UPRIGHT}
    b2 = {'rect':pygame.Rect(200, 200, 20, 20),
        'color':GREEN, 'dir':UPLEFT}
    b3 = {'rect':pygame.Rect(100, 150, 60, 60),
        'color':BLUE, 'dir':DOWNLEFT}
    boxes = [b1, b2, b3]

    pygame.init()

    WWIDTH  = 800 ; WHEIGHT = 300
    windowSurface = pygame.display.set_mode((WWIDTH,
                                        WHEIGHT))
    pygame.display.set_caption('Animation')

    windowSurface.fill(CUSTOM)


    pygame.draw.polygon(windowSurface, GREEN, 
                        ((146, 0), (291, 106),
                        (236, 277), (56, 277), (0, 106)))

    # Draw a couple of lines
    pygame.draw.line(windowSurface, BLUE, 
                    (60, 60), (120, 60), 4)
    pygame.draw.line(windowSurface, BLUE, 
                    (120, 60), (60, 120))

    # Draw a white circle
    pygame.draw.circle(windowSurface, WHITE, 
                    (300, 50), 50, 10)

    # Draw an ellipse
    pygame.draw.ellipse(windowSurface, BLACK, 
                        (300, 250, 40, 80), 1)

    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('Hello world!', True,
                            WHITE, BLUE)

    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery

    left = 200
    top = 100
    width = 50
    height = 200
    pygame.draw.rect(windowSurface, BLACK, textRect)

    windowSurface.blit(text, textRect)

    while True:
        windowSurface.fill(WHITE)

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

            if b['rect'].top < 0:
                # The box has moved past the top.
                if b['dir'] == UPLEFT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPRIGHT:
                    b['dir'] = DOWNRIGHT
            
            if b['rect'].bottom > WHEIGHT:
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

            if b['rect'].right > WWIDTH:
                # The box has moved past the right side.
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPRIGHT:
                    b['dir'] = UPLEFT
            
            pygame.draw.rect(windowSurface, b['color'], b['rect'])

        # Do something
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # update the window
        pygame.display.update()
        time.sleep(0.02)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())