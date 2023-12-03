import math
import string
import numpy as np

johns_matrix = open("input.txt").readlines() # variable's name is an old running joke
# johnathans_matrix = np.ndarray((len(input[0].removesuffix("\n")), len(input)), np.character)

for y, row in enumerate(johns_matrix):
    for x, char in enumerate(row):
        if char in string.punctuation and char != ".":
            adjacents = []
            for row2 in johns_matrix[y - 1:y + 2]:
                for char2 in row[x - 1:x + 2]:
                    adjacents.append(char2)
            adjacents.pop(4)  # this is a bad way of getting adjacents
            for adjacent in adjacents:
                if adjacent in string.digits:



