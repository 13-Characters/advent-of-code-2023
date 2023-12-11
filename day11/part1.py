input = [line.removesuffix("\n") for line in open("input.txt").readlines()]

empty_rows, empty_cols = [], []
for row_num in range(len(input)):
    row = input[row_num]
    if "#" not in row: empty_rows.append(row_num)
for col_num in range(len(input[0])):
    col = "".join([input[i][col_num] for i in range(len(input))])
    if "#" not in col: empty_cols.append(col_num)

galaxies = []
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append([x, y])

for i, galaxy in enumerate(galaxies):
    x, y = galaxy[0], galaxy[1]
    xOffset, yOffset = len([col for col in empty_cols if x > col]), len([row for row in empty_rows if y > row])
    galaxies[i] = [x + xOffset, y + yOffset]

result = 0
for i, a in enumerate(galaxies):
    for b in galaxies[i:]:
        if a != b:
            result += abs((b[1] - a[1])) + abs((b[0] - a[0]))
print(result)