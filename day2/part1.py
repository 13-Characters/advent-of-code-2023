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
    gamePossible = True
    for turn in game:
        if turn[0] > 12 or turn[1] > 13 or turn[2] > 14:
            gamePossible = False
            break
    if gamePossible:
        result += (i + 1) # game IDs start at 1
    else:
        print(i + 1, game)

print(result)

