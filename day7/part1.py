from functools import cmp_to_key
from collections import Counter
def compare(hand1: str, hand2: str):
    # Compare the types
    if max(Counter(hand1).values()) > max(Counter(hand2).values()):
        return 1
    if max(Counter(hand1).values()) < max(Counter(hand2).values()):
        return -1
    if max(Counter(hand1).values()) == max(Counter(hand2).values()):
        # Distinguishes between two-pair/one-pair and three-of-a-kind and Full house
        if len(Counter(hand1).values()) < len(Counter(hand2).values()):
            return 1
        if len(Counter(hand1).values()) > len(Counter(hand2).values()):
            return -1
    # Compare the cards
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    for i in range(len(hand1)):
        if cards.index(hand1[i]) < cards.index(hand2[i]):
            return 1
        if cards.index(hand1[i]) > cards.index(hand2[i]):
            return -1
    return 0
input = open("input.txt").readlines()
data = []
for line in input:
    card, bet = line.split()
    bet = int(bet)
    data.append((card, bet))

data.sort(key=cmp_to_key(lambda x, y: compare(x[0], y[0])))
result = 0
for r, line in enumerate(data):
    rank = r + 1
    bid = line[1]
    result += rank * bid
print(result)