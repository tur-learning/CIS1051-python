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

    pygame.init()

    windowSize = (800, 800)
    windowSurface = pygame.display.set_mode(windowSize)
    pygame.display.set_caption('My first videogame')

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

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())