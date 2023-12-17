input = open("input.txt")
input = input.readline().removesuffix("\n").split(",")

result = 0
for string in input:
    string = list(bytes(string, encoding="ascii"))
    hash = 0
    for char in string:
        hash += char
        hash *= 17
        hash %= 256
    result += hash
print(result)