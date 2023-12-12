import re
input = open("input.txt").readlines()
def determineArrangements(springs: str, numbers: list):
    if springs.count("?") == 0:
        return springs
    if springs.count("?") == 1:
        springsNew = springs.replace("?", "#")
        if [len(substr) for substr in re.findall("#+", springs)] == numbers:
            return springsNew
        springsNew = springs.replace("?", ".")
        if [len(substr) for substr in re.findall("#+", springs)] == numbers:
            return springsNew
    remaining = sum(numbers) - springs.count("#") # The remaining amount of broken springs needed for valid solution
    currentNumbers = [len(substr) for substr in re.findall("#+", springs)]
    end = 0
    for i, number in currentNumbers:
        if number != numbers[i]:
            end = i
            break
    for char in springs[:end]: # I have no idea if I am on the right track with this

result = 0
for line in input:
    springs, numbers = line.split(" ")
    numbers = numbers.split(",")
    result += determineArrangements(springs, numbers)
