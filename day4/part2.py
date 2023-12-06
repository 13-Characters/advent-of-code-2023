input = open("input.txt").readlines()
result = 0
def playCard(i):
    cardsWon = 0
    line = input[i]
    line = line.removeprefix(f"Card   {i+1}: ")
    line = line.removesuffix(f"\n")
    winning, card = line.split(" | ")
    winning_numbers = set([w for w in winning.split(" ") if w != "" and w != " "]) # list comprehension is in so nothing weird happens
    card_numbers = set([c for c in card.split(" ") if c != "" and c != " "])
    if len(winning_numbers & card_numbers) > 0:
        for a in range(i+1, i + len(winning_numbers & card_numbers) + 1):
            cardsWon += playCard(a)
    cardsWon += 1
    return cardsWon

for i in range(len(input)):
    result += playCard(i)

print(result)