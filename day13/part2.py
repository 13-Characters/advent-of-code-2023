import numpy as np
def reflectionTester(grid: list[list[str]]):
    for reflectionRow in range(len(grid)): # Test every reflection row
        leftHalf = grid[:reflectionRow]
        rightHalf = grid[reflectionRow:]
        if len(leftHalf) > len(rightHalf):
            leftHalf = leftHalf[-len(rightHalf):]
        if len(rightHalf) > len(leftHalf):
            rightHalf = rightHalf[:len(leftHalf)]
        matches = [left == right for left, right in zip(leftHalf, reversed(list(rightHalf)))]
        if matches.count(False) == 1: # Possible when there is one smudge
            index = matches.index(False)
            leftMismatch = leftHalf[index]
            rightMismatch = rightHalf[len(rightHalf) - 1 - index]
            if [leftChar == rightChar for leftChar, rightChar in zip(leftMismatch, rightMismatch)].count(False) == 1:
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