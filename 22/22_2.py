from collections import deque

with open("22_input.txt") as fin:
    data = fin.read().split("\n")

def score(deck):
    total = 0
    for i in range(len(deck)):
        total += deck[i] * (len(deck) - i)

    return total

def play_recursive_combat(deck1, deck2):
    #print("\n=== NEW GAME ===")
    #print("Player 1:", deck1)
    #print("Player 2:", deck2)

    total_cards = len(deck1) + len(deck2)

    history = set()

    while len(deck1) != total_cards and len(deck2) != total_cards:
        if (tuple(deck1), tuple(deck2)) in history:
            return 1, None
        history.add((tuple(deck1), tuple(deck2)))

        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if card1 <= len(deck1) and card2 <= len(deck2):
            deck1copy = deque(list(deck1)[:card1])
            deck2copy = deque(list(deck2)[:card2])
            subgame_result = play_recursive_combat(deck1copy, deck2copy)
            winner, _ = subgame_result

        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
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

winner, winning_deck = play_recursive_combat(deck1, deck2)

ans = score(winning_deck)
print(ans)