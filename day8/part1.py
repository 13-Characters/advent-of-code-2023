input = open("input.txt").readlines()
data = []
pointers = []
result = 0

for line in input[2:]:
    address, pointer = line.split(" = ")
    data.append(address)
    pointer = pointer.removeprefix("(")
    pointer = pointer.removesuffix("\n")
    pointer = pointer.removesuffix(")")
    pointers.append(tuple(pointer.split(", ")))

currentAddress = "AAA"
steps = 0
stop = False
while stop == False:
    for char in input[0].removesuffix("\n"):
        if char == "L":
            currentAddress = pointers[data.index(currentAddress)][0]
        if char == "R":
            currentAddress = pointers[data.index(currentAddress)][1]
        steps += 1
        if currentAddress == "ZZZ":
            stop = True
            break
print(steps)