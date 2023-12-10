import modified_horse_renderer
input = [i.removesuffix("\n") for i in open("input.txt").readlines()]

def addMidpoints(char, location):
    midpointDict = {"|": [(0, -0.5), (0, 0.5)], "-": [(-0.5, 0), (0.5, 0)], "L": [(0, -0.5), (0.5, 0)],
                  "J": [(0, -0.5), (-0.5, 0)], "7": [(0, 0.5), (-0.5, 0)], "F": [(0, 0.5), (0.5, 0)]}
    return [(m[0] + location[0], m[1] + location[1]) for m in midpointDict[char]]
def floodFill(locations):
    locations_new = locations.copy()
    # We are flood-filling lattice point and every point in between so we have to add midpoints to location
    for l in locations:
        midpoints = addMidpoints(input[l[1]][l[0]], l)
        for m in midpoints: locations_new.append(m)
    outside = []
    newlyAdded = [(0,0)]
    while len(newlyAdded) > 0:
        for i in newlyAdded:
            outside.append(i)
            adjacents = [(i[0] - 0.5, i[1]), (i[0] + 0.5, i[1]), (i[0], i[1] - 0.5), (i[0], i[1] + 0.5)]
            for adj in adjacents:
                if 0 <= adj[0] < len(input[0]) and 0 <= adj[1] < len(input) and adj not in outside and adj not in newlyAdded and adj not in locations_new:
                    newlyAdded.append(adj)
            newlyAdded.remove(i)
    outside = [(int(o[0]), int(o[1])) for o in outside if o[0] % 1 == 0 and o[1] % 1 == 0]
    return outside

def checkEnterability(location: tuple):
    result = []
    x = location[0]
    y = location[1]
    north, east, south, west = (x, y-1), (x+1, y), (x, y+1), (x-1, y)
    connects_north, connects_east, connects_south, connects_west = ["|", "J", "L", "S"], ["-", "L", "F", "S"], ["|", "7", "F", "S"], ["-", "7", "J", "S"]
    if input[north[1]][north[0]] in connects_south and input[y][x] in connects_north:
        result.append(north)
    if input[east[1]][east[0]] in connects_west and input[y][x] in connects_east:
        result.append(east)
    if input[south[1]][south[0]] in connects_north and input[y][x] in connects_south:
        result.append(south)
    if input[west[1]][west[0]] in connects_east and input[y][x] in connects_west:
        result.append(west)
    return tuple(result)


starting_location = ()
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "S":
            starting_location = (x, y)
# Replace S with corresponding pipe
neighbors = checkEnterability(starting_location)
# North
if (starting_location[0], starting_location[1] - 1) in neighbors:
    if (starting_location[0] + 1, starting_location[1]) in neighbors:
        input[starting_location[1]] = input[starting_location[1]].replace("S", "L")
    if (starting_location[0] - 1, starting_location[1]) in neighbors:
        input[starting_location[1]] = input[starting_location[1]].replace("S", "J")
    if (starting_location[0], starting_location[1] + 1) in neighbors:
        input[starting_location[1]] = input[starting_location[1]].replace("S", "|")
# South
if (starting_location[0], starting_location[1] + 1) in neighbors:
    if (starting_location[0] + 1, starting_location[1]) in neighbors:
        input[starting_location[1]] = input[starting_location[1]].replace("S", "F")
    if (starting_location[0] - 1, starting_location[1]) in neighbors:
        input[starting_location[1]] = input[starting_location[1]].replace("S", "7")
# East-West
if (starting_location[0] + 1, starting_location[1]) in neighbors and (starting_location[0] - 1, starting_location[1]) in neighbors:
    input[starting_location[1]] = input[starting_location[1]].replace("S", "-")
locations = [starting_location, neighbors[0]]

while locations[-1] != starting_location:
    newLocations = checkEnterability(locations[-1])
    for newLocation in newLocations:
        if newLocation != locations[-2]:
            locations.append(newLocation)
            break

print(len(locations) // 2) # gives the middle index of the list which is just the furthest dist
locations.pop() # Last index is just the starting location again
modified_horse_renderer.renderFrame(input, locations, [], "part1")
flood_fill = floodFill(locations)
modified_horse_renderer.renderFrame(input, locations, flood_fill, "part2")
print((len(input[0]) * len(input)) - len(flood_fill) - len(locations))