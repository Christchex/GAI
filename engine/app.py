import pygame
import sys
import math
from species import Species
import json
from json import JSONDecoder
from pygame.locals import *

def loadSpeciesFile(file):
    assert(file.endswith(".json"))
    data = JSONDecoder().decode(json.dumps(json.loads(open(file, 'r').read())))
    return Species(data)

def main():
    pygame.init()

    FPS = 30
    fpsClock = pygame.time.Clock()

# Setup the window
    DISPLAY_SURF = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mothafuckin' Ant DEMO!!!")

# Setup colors
    BLACK = ( 0, 0, 0 )
    WHITE = ( 255, 255, 255 )
    RED = ( 255, 0, 0 )
    GREEN = ( 0, 255, 0 )
    BLUE = ( 0, 0, 255 )

# Draw text
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 300)

# import ant
    ant = loadSpeciesFile("ant.json")
    antImg = pygame.image.load(ant.getImage())
    antImg = pygame.transform.rotate(antImg, -90)
    antX = 10
    antY = 10
    direction = 'right'

# main game loop
    while True:
        DISPLAY_SURF.fill(WHITE)
        DISPLAY_SURF.blit(textSurfaceObj, textRectObj)

        if direction == 'right':
            antX += ant.moveSpeed
            if antX == 680:
                direction = 'down'
                antImg = pygame.transform.rotate(antImg, -90)
        elif direction == 'down':
            antY += ant.moveSpeed
            if antY == 520:
                direction = 'left'
                antImg = pygame.transform.rotate(antImg, -90)
        elif direction == 'left':
            antX -= ant.moveSpeed
            if antX == 10:
                direction = 'up'
                antImg = pygame.transform.rotate(antImg, -90)
        elif direction == 'up':
            antY -= ant.moveSpeed
            if antY == 10:
                direction = 'right'
                antImg = pygame.transform.rotate(antImg, -90)

        DISPLAY_SURF.blit(antImg, (antX, antY))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
