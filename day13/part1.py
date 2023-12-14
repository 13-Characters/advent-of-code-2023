import numpy as np
def reflectionTester(grid: list[list[str]]):
    reflectionRow = -1
    # Find potential reflection line
    for i, row in enumerate(grid):
        if row not in grid[i+1:]:
            continue
        else:
            j = -1
            # Case 1: the reflection line is above the middle of the grid
            if i == 0:
                j = grid.index(row, i+1)
            # Case 2: the reflection line is below the middle of the grid
            if grid[-1] == row and i != 0:
                j = len(grid) - 1
            if j != -1:
                reflectionRow = (i + j) // 2 + 1
                # Confirm that this horizontal line is a valid reflection line
                leftHalf = grid[:reflectionRow]
                rightHalf = grid[reflectionRow:]
                if len(leftHalf) > len(rightHalf):
                    leftHalf = leftHalf[-len(rightHalf):]
                if len(rightHalf) > len(leftHalf):
                    rightHalf = rightHalf[:len(leftHalf)]
                if leftHalf == list(reversed(rightHalf)):
                    return reflectionRow
    return -1

input = open("input.txt").readlines()
parsedInput = [[]]
for line in input:
    if line == "\n":
        parsedInput.append([])
    else:
        parsedInput[-1].append(list(line.removesuffix("\n")))

result = 0
for grid in parsedInput:
    if reflectionTester(grid) != -1:
        result += 100 * reflectionTester(grid)
    else:
        grid = [list(x) for x in np.array(grid).transpose()]
        if reflectionTester(grid) != -1:
            result += reflectionTester(grid)
print(result)