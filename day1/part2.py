import numpy as np
import math
import string

def convertLine(line):
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # Note: This only works because there's always a digit in every line
    firstDigit = [char for char in line if char in string.digits][0] # Gets the first character digit from the line
    lowestInd = line.find(firstDigit)
    for digit in digits:
        if line.find(digit) != -1 and line.find(digit) < lowestInd:
            lowestInd = line.find(digit)
            firstDigit = digits.index(digit)

    lastDigit = [char for char in line if char in string.digits][-1]
    highestInd = line.rfind(lastDigit)
    for digit in digits:
        if line.rfind(digit) != -1 and line.rfind(digit) > highestInd:
            highestInd = line.rfind(digit)
            lastDigit = digits.index(digit)
    return int(firstDigit) * 10 + int(lastDigit)

input = open("input.txt").readlines()

for i, line in enumerate(input):
    input[i] = convertLine(line)

result = sum(input)
print(result)
