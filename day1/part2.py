import numpy as np
import math
import string

def deleteDigits(line):
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lowestInd = math.inf
    digitToRemove = ""
    for digit in digits:
        if line.find(digit) != -1 and line.find(digit) < lowestInd:
            lowestInd = line.find(digit)
            digitToRemove = digit
    if lowestInd != math.inf:
        line = line[:lowestInd] + str(digits.index(digitToRemove)) + line[lowestInd + len(digitToRemove):]

    highestInd = -math.inf
    digitToRemove = ""
    for digit in digits:
        if line.rfind(digit) != -1 and line.find(digit) > highestInd:
            highestInd = line.rfind(digit)
            digitToRemove = digit
    if highestInd != -math.inf:
        line = line[:highestInd] + str(digits.index(digitToRemove)) + line[highestInd + len(digitToRemove):]
    return line

input = open("input.txt").readlines()

for i, line in enumerate(input):
    input[i] = deleteDigits(line)

for i, line in enumerate(input):
    line_list = []
    for char in line:
        if char in string.digits:
            line_list.append(char)
    input[i] = ''.join(line_list)

result = 0
for number in input:
    ones_place = int(number[-1])
    tens_place = int(number[0]) * 10
    result += ones_place
    result += tens_place
print(result)
