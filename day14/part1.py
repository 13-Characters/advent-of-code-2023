def updateRockPositions(rounds: list[(int, int)]):
    # Note: rounds must be sorted by y-value in ascending order
    for i, round in enumerate(rounds):
        roundX, roundY = round[0], round[1]
        newY = 0
        for y in range(roundY - 1, -1, -1):
            if input[y][roundX] == "#" or (roundX, y) in rounds:
                newY = y + 1
                break
        rounds[i] = (roundX, newY)
    return rounds
input = [line.removeprefix("\n") for line in open("input.txt").readlines()]
roundRockPositions = []
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "O":
            roundRockPositions.append((x, y))

newPositions = updateRockPositions(roundRockPositions)
print(sum([len(input) - rock[1] for rock in newPositions]))