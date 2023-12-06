input = open("input.txt")
def xToYMap(inputInt: int, map: list) -> int:
    # map is a list with structure like [(234, 212, 583), (432, 249, 103), ...]
    for m in map:
        if inputInt in range(m[1], m[1]+m[2]):
            return m[0] + (inputInt - m[1])
    return inputInt

listOfMaps = []
seeds = [int(i) for i in input.readline().split(":")[1].split()]
for line in input:
    if line.find("map") != -1:
        listOfMaps.append([])
    else:
        if line != "\n":
            listOfMaps[-1].append(tuple(int(i) for i in line.split()))

locations = []
for seed in seeds:
    location = seed
    for map in listOfMaps:
        location = xToYMap(location, map)
    locations.append(location)
print(seeds)
print(locations)
print(min(locations))