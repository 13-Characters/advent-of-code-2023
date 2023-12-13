import numpy as np
def verticalReflectionTester(grid: list[str][str]):
    # Find potential reflection line
    for i, row in grid:

input = open("example_input.txt").readlines()
parsedInput = [[]]
for line in input:
    if line == "\n":
        parsedInput.append([])
    else:
        parsedInput[-1].append(line.removesuffix("\n"))