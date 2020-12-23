from collections import deque

with open("22_input.txt") as fin:
    data = fin.read().split("\n")

def score(deck):
    total = 0
    for i in range(len(deck)):
        total += deck[i] * (len(deck) - i)

    return total

def play_combat(deck1, deck2):
    total_cards = len(deck1) + len(deck2)

    while len(deck1) != total_cards and len(deck2) != total_cards:
        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    if len(deck1) == total_cards:
        return 1, deck1
    return 2, deck2

deck1 = deque()
deck2 = deque()

index = 1
while data[index] != "":
    deck1.append(int(data[index]))
    index += 1

index += 2
while index < len(data):
    deck2.append(int(data[index]))
    index += 1

winner, winning_deck = play_combat(deck1, deck2)

ans = score(winning_deck)
print(ans)