import time
def evalHeatLoss(path: list):
    result = 0
    for block in path:
        blockX, blockY = block[0], block[1]
        result += int(grid[blockY][blockX])
    return result
def evalPath(startingPosition: tuple, instructions: str):
    # F = forwards, L = turn left, R = turn right
    result = [startingPosition]
    # 0=north, 1=east, 2=south, 3=west
    if instructions[0] == "E": direction = 1
    if instructions[0] == "S": direction = 2
    vectors = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for char in instructions[1:]:
        x, dx = result[-1][0], vectors[direction][0]
        y, dy = result[-1][1], vectors[direction][1]
        if char == "F":
            result.append((x + dx, y + dy))
        if char == "L":
            direction = (direction - 1) % 4
        if char == "R":
            direction = (direction + 1) % 4
    return result
grid = [list(line.removesuffix("\n")) for line in open("input.txt").readlines()]
heatLossDict = {}
endingPositionDict = {}
n = 5
for i in range(6 ** n): # Generates all possible starting paths with 6 turns (there are 93312)
    path = ""
    for j in range(n):
        numberOfSteps = i % 3
        leftOrRight = i % 2
        path += "F" * (numberOfSteps+1)
        if leftOrRight == 0: path += "L"
        if leftOrRight == 1: path += "R"
        i = i // 6
    # Case 1: we start going east
    eval = evalPath((0,0), "E" + path)
    if eval[-1][0] >= 0 and eval[-1][1] >= 0:
        heatLossDict["E" + path] = evalHeatLoss(eval)
        endingPositionDict["E" + path] = eval[-1]
    # Case 2: we start going south
    eval = evalPath((0, 0), "S" + path)
    if eval[-1][0] >= 0 and eval[-1][1] >= 0:
        heatLossDict["S" + path] = evalHeatLoss(eval)
        endingPositionDict["S" + path] = eval[-1]

start_time = time.time()
# Only keep the best distances
threshold = min(sorted([coord[0] + coord[1] for coord in endingPositionDict.values()], reverse=True)[0:500])
popList = []
for key in endingPositionDict:
    if endingPositionDict[key][0] + endingPositionDict[key][1] < threshold:
        popList.append(key)
for key in popList:
    endingPositionDict.pop(key)
    heatLossDict.pop(key)

# Sorry if this crosses the border
border = max(sorted(list(heatLossDict.values()))[0:100])
popList = []
for key in heatLossDict:
    if heatLossDict[key] > border:
        popList.append(key)
for key in popList:
    endingPositionDict.pop(key)
    heatLossDict.pop(key)

runLoop = True
while runLoop:
    heatLossCopy = heatLossDict.copy()
    endingPositionCopy = endingPositionDict.copy()
    for i in range(6 ** n):  # Generates all possible starting paths with 6 turns (there are 93312)
        path = ""
        k = i
        for j in range(n):
            numberOfSteps = k % 3
            leftOrRight = k % 2
            path += "F" * (numberOfSteps + 1)
            if leftOrRight == 0: path += "L"
            if leftOrRight == 1: path += "R"
            k = k // 6
        temp = []
        for key in heatLossCopy.keys():
            eval = evalPath((0, 0), key + path)
            temp.append((key + path, evalHeatLoss(eval), eval[-1]))
        for t in temp:
            heatLossDict[t[0]] = t[1]
            endingPositionDict[t[0]] = t[2]
    threshold = min(sorted([coord[0] + coord[1] for coord in endingPositionDict.values()], reverse=True)[0:500])
    popList = []
    for key in endingPositionDict:
        if endingPositionDict[key][0] + endingPositionDict[key][1] < threshold:
            popList.append(key)
    for key in popList:
        endingPositionDict.pop(key)
        heatLossDict.pop(key)
    # Sorry if this crosses the border
    border = max(sorted(list(heatLossDict.values()))[0:100])
    popList = []
    for key in heatLossDict:
        if heatLossDict[key] > border:
            popList.append(key)
    for key in popList:
        endingPositionDict.pop(key)
        heatLossDict.pop(key)
    # If 2/3rds of the ending positions are at the end point
    if [coord == (len(grid[0]) - 1, len(grid) - 1) for coord in endingPositionDict.values()].count(True) > (2 * len(endingPositionDict) / 3):
        runLoop = False

print(min(heatLossDict.values()))