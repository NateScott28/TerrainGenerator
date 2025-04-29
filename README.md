# TerrainGenerator
Python Project that creates terrain by smoothing random noise

To run, simply download the python file and execute it. To alter the way the terrain looks, here is a list of the differenet varialbes that can be changed and what they do:

width, height = 600, 700        # Size of window in pixels
gridSize = 300                  # Height and Width of grid in tiles
tileSize = width / gridSize     # Pixel size of 1 tile
smoothness = 8                  # Number of times smooth() is run                           *INCREASE FOR SMOOTHER LOOKING MAP*
waterLevel = 67                 # Alt level at which anything below is considered water     *INCREASE FOR LESS WATER*
mountianLevel = 74              # level where anything above is a mountain                  *INCREASE FOR MORE LAND, LESS MOUNTAIN*
edgeValue = 0                   # The value of all edge tiles                               *INCREASE FOR LESS WATER*
altitudeMax = 150               # Max value that a tiles altitude can be                    *INCREASE FOR MORE LAND*
