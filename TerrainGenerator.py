'''
' Author: Nathan Scott 
' Date: 12/11/19
' Purpose: Terrain Generator
'''
import sys
import pygame
import time
import random
from pygame.locals import *

width, height = 600, 700
gridSize = 300                  # Height and width of grid
tileSize = width / gridSize     # Pixel size of 1 tile
smoothness = 8                  # Number of times smooth() is run                           ***INCREASE FOR LESS NOISE***
waterLevel = 67                 # Alt level at which anything below is considered water     ***INCREASE FOR LESS WATER***
mountianLevel = 74
edgeValue = 0                   # The value of all edge tiles                               ***INCREASE FOR LESS WATER***
altitudeMax = 150               # Max value that a tiles altitude can be                    ***INCREASE FOR MORE LAND ***

#Colors
GRASS = (102, 219, 79)
WATER = (79, 170, 219)
SAND = (255, 224, 102)
MOUNTAIN = (160, 163, 168)

#BUTTON = (255,255,255)
'''
' Class contains each Tile of the grid
' Holds information on location of the node, 
'''
class Tile():
    def __init__(self, x, y):

        #position
        self.x = x
        self.y = y
        
        #altitude of tile
        self.alt = random.randint(0, altitudeMax)

'''### Main Method ###'''
def main():

    pygame.init()
    Window = pygame.display.set_mode((width, height))

    grid = []

    for y in range(gridSize):
        row = []
        for x in range(gridSize):
            row.append(Tile(x, y))
        grid.append(row)

    for i in range(smoothness):
        smooth(grid)


    #button = pygame.rect(Window, BUTTON, ((gridSize // 2) - 40, 620, 80, 40))
    while True:
        update(Window, grid)
        draw(Window, grid)

'''### Smooths the noise into the '''
def smooth(grid):
    for y in range(gridSize):
        for x in range(gridSize):
            if(y == 0 or y == gridSize - 1 or x == 0 or x == gridSize - 1):
                grid[x][y].alt = edgeValue

            else: 
                #grid[x][y].alt = (gridSize // 2) - ((((x - gridSize//2)**2 + (y - gridSize//2)**2)**0.5) //1000)
                grid[x][y].alt = (grid[x - 1][y - 1].alt + grid[x][y - 1].alt + grid[x + 1][y - 1].alt + 
                                  grid[x - 1][y].alt + grid[x + 1][y].alt + grid[x][y].alt + grid[x - 1][y + 1].alt + grid[x][y + 1].alt + grid[x + 1][y + 1].alt) // 9
                
                #Adds more altiutde to tiles closer to the center
                
def randomize(grid): 
    for y in range(gridSize):
        for x in range(gridSize):                
            grid[x][y].alt = random.randint(0, altitudeMax)

'''### Update Method ###'''
def update(Window, grid):
    for event in pygame.event.get():
        
        #On EXIT, close window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                randomize(grid)
                for i in range(smoothness):
                    smooth(grid)
'''
'''### Draw Method ###'''
def draw(Window, grid):
    
    #Re-render Button
    #pygame.draw.rect(button)

    tileColor = (102, 219, 79)
    for y in range(gridSize):
        for x in range(gridSize):
            if (grid[x][y].alt < waterLevel) or x == 0 or x == gridSize or y == 0 or y == gridSize: 
                tileColor = WATER
            
            elif grid[x][y].alt < mountianLevel:     
                if((grid[x + 1][y].alt < waterLevel) or (grid[x - 1][y].alt < waterLevel) or (grid[x][y + 1].alt < waterLevel) or (grid[x][y - 1].alt < waterLevel)):
                    tileColor = SAND
                else: 
                    tileColor = GRASS
            else: 
                tileColor = MOUNTAIN


            pygame.draw.rect(Window, tileColor, ((x * tileSize), (y * tileSize), tileSize, tileSize))

    pygame.display.flip()

if __name__ == "__main__":
    main()