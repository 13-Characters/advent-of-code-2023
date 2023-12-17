from enum import Enum
import time
class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
def updateRockPositions(rounds: list[(int, int)], direction: Direction):
    for i, round in enumerate(rounds):
        roundX, roundY = round[0], round[1]
        if direction == Direction.NORTH or direction == Direction.SOUTH:
            newY = 0
            if direction == Direction.NORTH:
                for y in range(roundY - 1, -1, -1):
                    if input[y][roundX] == "#" or (roundX, y) in rounds:
                        newY = y + 1
                        break
            if direction == Direction.SOUTH:
                newY = len(input) - 1
                rounds = list(reversed(rounds))
                for y in range(roundY + 1, len(input)):
                    if input[y][roundX] == "#" or (roundX, y) in rounds:
                        newY = y - 1
                        break
            rounds[i] = (roundX, newY)
        if direction == Direction.EAST or direction == Direction.WEST:
            newX = 0
            if direction == Direction.EAST:
                rounds = sorted(rounds, key=lambda x: x[0], reverse=True)
                for x in range(roundX + 1, len(input[0])):
                    if input[roundY][x] == "#" or (x, roundY) in rounds:
                        newX = x - 1
                        break
            if direction == Direction.WEST:
                newX = len(input[0]) - 1
                rounds = sorted(rounds, key=lambda x: x[0])
                for x in range(roundX - 1, -1, -1):
                    if input[roundY][x] == "#" or (x, roundY) in rounds:
                        newX = x + 1
                        break
            rounds[i] = (newX, roundY)
    return rounds
input = [line.removeprefix("\n") for line in open("example_input.txt").readlines()]
roundRockPositions = []
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "O":
            roundRockPositions.append((x, y))
start_time = time.time()
# The one cycle
newPositions = updateRockPositions(roundRockPositions, Direction.NORTH)
newPositions = updateRockPositions(roundRockPositions, Direction.WEST)
newPositions = updateRockPositions(roundRockPositions, Direction.SOUTH)
newPositions = updateRockPositions(roundRockPositions, Direction.EAST)
print(f"{time.time() - start_time} seconds per cycle")
print(sum([len(input) - rock[1] for rock in newPositions]))
for line in input:
    printedLine = line.replace("O", ".")
    