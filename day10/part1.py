
input = [i.removeprefix("\n") for i in open("input.txt").readlines()]

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

locations = [starting_location, checkEnterability(starting_location)[0]]

while locations[-1] != starting_location:
    newLocations = checkEnterability(locations[-1])
    for newLocation in newLocations:
        if newLocation != locations[-2]:
            locations.append(newLocation)
            break

print(len(locations) // 2) # gives the middle index of the list which is just the furthest dist