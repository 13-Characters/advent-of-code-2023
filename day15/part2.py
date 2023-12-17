import re
input = open("input.txt")
input = input.readline().removesuffix("\n").split(",")

result = 0
hashes = []
boxes = [[] for i in range(256)]
for string in input:
    label = re.match(r"[a-z]+", string).group(0)

    labelAscii = list(bytes(label, encoding="ascii"))
    hash = 0
    for char in labelAscii:
        hash += char
        hash *= 17
        hash %= 256
    if "=" in string:
        focalLength = string[-1]
        lens = (label, focalLength)
        if label in [lens[0] for lens in boxes[hash]]:
            removedLabelIndex = [lens[0] for lens in boxes[hash]].index(label)
            boxes[hash].pop(removedLabelIndex)
            boxes[hash].insert(removedLabelIndex, lens)
        else:
            boxes[hash].append(lens)
    if "-" in string:
        if label in [lens[0] for lens in boxes[hash]]:
            removedLabelIndex = [lens[0] for lens in boxes[hash]].index(label)
            boxes[hash].pop(removedLabelIndex)
    hashes.append(hash)
result = 0
for n, box in enumerate(boxes):
    for i, lens in enumerate(box):
        result += (n + 1) * (i + 1) * int(lens[1])
print(result)