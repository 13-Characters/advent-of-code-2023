import math

# 0 = red, 1 = green, 2 = blue
input = open("input.txt").readlines()
data = []

# Convert the input into a nested list thing
for i, line in enumerate(input):
    line = line.removeprefix(f"Game {i+1}: ")
    line = line.removesuffix(f"\n")
    game = line.split("; ")
    gameData = []
    for turn in game:
        numColorList = turn.split(", ")
        turnData = [0, 0, 0]
        for numColor in numColorList:
            num, color = numColor.split(" ")
            if color == "red":
                turnData[0] = int(num)
            if color == "green":
                turnData[1] = int(num)
            if color == "blue":
                turnData[2] = int(num)
        gameData.append(turnData)
    data.append(gameData)

# Note: the IDs of the games starts at 1
result = 0
for i, game in enumerate(data):
    redMax = max(turn[0] for turn in game)
    greenMax = max(turn[1] for turn in game)
    blueMax = max(turn[2] for turn in game)
    result += redMax * greenMax * blueMax

print(result)

