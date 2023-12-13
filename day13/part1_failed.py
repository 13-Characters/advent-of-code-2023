import numpy as np
def sequences_helper(l: list):
    previous = None
    result = []
    for i in l:
        if i == previous:
            result[-1][1] += 1
        if i != previous:
            result.append([i, 1])
        previous = i
    return [tuple(x) for x in result]
input = open("example_input.txt").readlines()
parsedInput = [[]]
for line in input:
    if line == "\n":
        parsedInput.append([])
    else:
        parsedInput[-1].append(line.removesuffix("\n"))

result = 0
counter_temporary = 0
for grid in parsedInput:
    counter_temporary += 1
    grid = [list(str) for str in grid]
    reflectionRows = []
    for i, row in enumerate(grid):
        if row not in grid[i+1:]:
            reflectionRows.append(-1)
            continue
        j = len(grid) - list(reversed(grid)).index(row) - 1
        reflectionRows.append((i + j) // 2 + 1)
    sq = sequences_helper(reflectionRows)
    if [s[0] for s in sq] != [-1]:
        if max([s[1] for s in sq if s[0] != -1]) >= 2:
            # My code gets more and more mystical as the days progress I can't even properly explain this
            index = [s[1] for s in sq].index(max([s[1] for s in sq if s[0] != -1]))
            horizontalLine = [s[0] for s in sq][index]
            if horizontalLine != -1:
                result += 100 * horizontalLine
                print(f"Grid {counter_temporary}: Horizontal line found, {horizontalLine} rows above")

    gridTranspose = list(np.array(grid).transpose())
    gridTranspose = [list(str) for str in gridTranspose]
    reflectionCols = []
    for i, col in enumerate(gridTranspose):
        if col not in gridTranspose[i + 1:]:
            reflectionCols.append(-1)
            continue
        j = len(gridTranspose) - list(reversed(gridTranspose)).index(col) - 1
        reflectionCols.append((i + j) // 2 + 1)
    sq = sequences_helper(reflectionCols)
    if [s[0] for s in sq] != [-1]:
        if max([s[1] for s in sq if s[0] != -1]) >= 2:
            # My code gets more and more mystical as the days progress I can't even properly explain this
            index = [s[1] for s in sq].index(max([s[1] for s in sq if s[0] != -1]))
            verticalLine = [s[0] for s in sq][index]
            if verticalLine != -1:
                result += verticalLine
                print(f"Grid {counter_temporary}: Vertical line found, {verticalLine} cols left")

print(result)