import random


cards = ["Jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

coin = choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)

print(number)
