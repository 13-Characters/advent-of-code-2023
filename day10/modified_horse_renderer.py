# Finally horse renderer runs at a speed that I am satisfied with
import glob
import os.path
import time
from multiprocessing import Pool
from PIL import Image
from tkinter import filedialog
import numpy as np

# AFAIK there is no clever formula to get the number if given adjacent pixels
# Based on this template https://github.com/sp614x/optifine/blob/master/OptiFineDoc/doc/images/ctm_template.png
def getCTMNumber(pixel, grid):
    caseDictionary = {"|": 24, "-": 2, "L": 16, "J": 17, "7": 5, "F": 4, ".": 26, "S": 0}
    char = grid[pixel[1]][pixel[0]]
    return caseDictionary[char]

def renderFrame(input, locations, outside, filename):
    colors = ["blue", "red", "white"]
    textures = {color: [Image.open(f"{color}/{i}.png") for i in range(47)] for color in colors}

    renderedFrame = Image.new("RGBA", (len(input[0]) * 32, len(input) * 32))
    grid = input
    for y in range(len(input)):
        for x in range(len(input[0])):
            if (x, y) in locations:
                colorName = "red"
            else:
                if (x, y) in outside:
                    colorName = "blue"
                else:
                    colorName = "white"
            renderedSquare = textures[colorName][getCTMNumber((x, y), grid)]
            renderedFrame.paste(renderedSquare, box=(x*32, y*32))
    renderedFrame.save(f"{filename}.png")