import math
import string
import numpy as np

johns_matrix = open("input.txt").readlines() # variable's name is an old running joke
# johnathans_matrix = np.ndarray((len(input[0].removesuffix("\n")), len(input)), np.character)

number_positions = []
numbers = []
length = 0
for y, row in enumerate(johns_matrix):
    for x, char in enumerate(row):
        if char in string.digits:
            if length == 0:
                number_positions.append([x, y, length + 1]) # These are how all the digit positions are stored
                numbers.append(int(char)) # These are how the numbers will be stored
            else:
                (number_positions[-1])[2] += 1
                numbers[-1] = numbers[-1] * 10 + int(char)
            length += 1
        else: length = 0

indicesToRemove = []
for i in range(len(number_positions)):
    number_position = number_positions[i]
    number = numbers[i]
    numberIsValid = False
    for y in range(number_position[1]-1, number_position[1]+2):
        for x in range(number_position[0]-1, number_position[0]+number_position[2]+1):
            if (0 <= x < len(johns_matrix[0].removesuffix("\n")) and 0 <= y < len(johns_matrix)
                    and johns_matrix[y][x] in string.punctuation and johns_matrix[y][x] != "."):
                numberIsValid = True
                break
    if not numberIsValid:
        indicesToRemove.append(i)

for index in reversed(indicesToRemove):
    number_positions.pop(index)
    numbers.pop(index)

print(numbers)
print(sum(numbers))

