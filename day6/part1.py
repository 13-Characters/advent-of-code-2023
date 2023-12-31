import math
input = open("input.txt").readlines()
times = [int(i) for i in input[0].split(":")[1].split()]
distances = [int(i) for i in input[1].split(":")[1].split()]
result = 1
for t, d in zip(times, distances):
    min = math.ceil((t / 2) - (math.sqrt(t ** 2 - 4 * d) / 2)) # Ironic
    max = math.floor((t / 2) + (math.sqrt(t ** 2 - 4 * d) / 2)) + 1 # Plus 1 because range() is weird
    result *= len(range(min, max))
print(result)