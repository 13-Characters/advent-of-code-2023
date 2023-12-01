import numpy as np
import math
import string

# input = open("input.txt")
input = open("input.txt").readlines()

for i, line in enumerate(input):
    line_list = []
    for char in line:
        if char in string.digits:
            line_list.append(char)
    input[i] = int(''.join(line_list))

result = 0
for number in input:
    ones_place = number % 10
    tens_place = (number // 10 ** math.floor(math.log10(number))) * 10
    result += ones_place
    result += tens_place
print(result)
