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
            derivatives[index].append(derivatives[index][-1] + derivatives[index + 1][-1])
        else:
            derivatives[index].append(0)
    result += derivatives[0][-1]

print(result)

