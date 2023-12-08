from math import lcm
input = open("input.txt").readlines()
data = []
pointers = []
result = 0

def runUntilZ(step: int, node: str):
    currentAddress = node
    stop = False
    steps = step
    while not stop:
        instructions = input[0].removesuffix("\n")
        char = instructions[steps % len(instructions)]
        if char == "L":
            currentAddress = pointers[data.index(currentAddress)][0]
        if char == "R":
            currentAddress = pointers[data.index(currentAddress)][1]
        steps += 1
        if currentAddress.endswith("Z"):
            return (steps, currentAddress)


for line in input[2:]:
    address, pointer = line.split(" = ")
    data.append(address)
    pointer = pointer.removeprefix("(")
    pointer = pointer.removesuffix("\n")
    pointer = pointer.removesuffix(")")
    pointers.append(tuple(pointer.split(", ")))

startingNodes = []
for node in data:
    if node.endswith("A"):
        startingNodes.append(node)
stepsList = []
cycleLengths = []
for i, node in enumerate(startingNodes):
    stepsList.append(runUntilZ(0, node))

print(lcm(*[s[0] for s in stepsList])) # it will take N steps for a ghost to return to a node that ends in "Z"
# where N is the number of steps it took to get there in the first place
# It took me like 30 minutes to find this