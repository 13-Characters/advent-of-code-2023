import math
input = open("input.txt").readlines()

def differentiate(nums: list):
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i + 1] - nums[i])
    return result

result = 0
for line in input:
    derivatives = []
    derivatives.append([int(i) for i in line.split()])
    while not all([i == 0 for i in derivatives[-1]]):
        derivatives.append(differentiate(derivatives[-1]))
    for i in range(len(derivatives)):
        index = len(derivatives) - 1 - i
        if i != 0:
            derivatives[index].insert(0, derivatives[index][0] - derivatives[index + 1][0])
        else:
            derivatives[index].insert(0, 0)
    result += derivatives[0][0]

print(result)

