import pygame, sys
import asyncio
from pygame.locals import *

async def main():
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    CUSTOM = (255, 125, 0)

    DOWNLEFT  = 'downleft'
    DOWNRIGHT = 'downright'
    UPLEFT    = 'upleft'
    UPRIGHT   = 'upright'
    MOVESPEED = 1

    pygame.init()

    WINDOWWIDTH = 800
    WINDOWHEIGHT = 800
    windowSize = (WINDOWWIDTH, WINDOWHEIGHT)
    windowSurface = pygame.display.set_mode(windowSize)
    pygame.display.set_caption('Bouncing boxes')

    windowSurface.fill(CUSTOM)

    # drawing a polygon on the main surface
    pygame.draw.polygon(windowSurface, GREEN, 
                        ((146, 0), (291, 106),
                        (236, 277), (56, 277), (0, 106)))

    pygame.draw.line(windowSurface, 
                    BLUE, 
                    (60, 60), 
                    (120, 60), 
                    4)
    pygame.draw.line(windowSurface, BLUE, 
                    (120, 60), (60, 120))

    pygame.draw.circle(windowSurface, WHITE, 
                    (300, 50), 20, 10)

    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('Hello world!', True, WHITE, BLUE)

    textRect = text.get_rect()

    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery

    windowSurface.blit(text, textRect)

    # declaring a few boxes
    b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
    b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
    b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
    boxes = [b1, b2, b3]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        windowSurface.fill(CUSTOM)

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
            
            pygame.draw.rect(windowSurface, b['color'], b['rect'])

        pygame.display.update()
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())