import math
input = open("input.txt").readlines()
print(math.prod([len(range(math.ceil((t/2)-(math.sqrt(t**2-4*d)/2)),math.floor((t / 2)+(math.sqrt(t**2-4*d)/2))+1))for t,d in zip([int(i)for i in input[0].split(":")[1].split()],[int(i)for i in input[1].split(":")[1].split()])]))