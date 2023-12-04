input = open("input.txt").readlines()
result = 0
for i, line in enumerate(input):
    line = line.removeprefix(f"Card   {i+1}: ")
    line = line.removesuffix(f"\n")
    winning, card = line.split(" | ")
    winning_numbers = set([w for w in winning.split(" ") if w != "" and w != " "]) # list comprehension is in so nothing weird happens
    card_numbers = set([c for c in card.split(" ") if c != "" and c != " "])
    if len(winning_numbers & card_numbers) > 0:
        card_value = 1 << (len(winning_numbers & card_numbers) - 1)
    else: card_value = 0
    result += card_value
print(result)