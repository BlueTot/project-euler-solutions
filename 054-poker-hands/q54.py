from collections import Counter

with open("poker.txt", "r") as f:
    poker = [line.split() for line in f.readlines()]

ranks = ["high card", "one pair", "two pairs", "three of a kind", "straight", "flush", "full house", "four of a kind", "straight flush", "royal flush"]

def player1_hand(line):
    cards = "".join([s[0] for s in line[:5]])
    suites = "".join([s[1] for s in line[:5]])
    return cards, suites

def player2_hand(line):
    cards = "".join([s[0] for s in line[5:]])
    suites = "".join([s[1] for s in line[5:]])
    return cards, suites

def card_value(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    elif card == "T":
        return 10
    else:
        return int(card)

def tie_break(line, player):
    cards = player1_hand(line)[0] if player == 1 else player2_hand(line)[0]
    scards = [card_value(card) for card in cards if cards.count(card) != 1]
    sorted_non1s = list({k: v for k, v in sorted(Counter(scards).items(), key=lambda item: item[1], reverse=True)}.keys())
    ones = [card_value(card) for card in cards if cards.count(card) == 1]
    return sorted_non1s + sorted(ones, reverse=True)


def hand_value(line, player):
    cards, suites = player1_hand(line) if player == 1 else player2_hand(line)
    unique_cards, unique_suites = set(cards), set(suites)
    if len(unique_cards) == 5: # high card, straight, flush, straight flush, royal flush
        if "A" in unique_cards and "K" in unique_cards and "Q" in unique_cards and "J" in unique_cards and "T" in unique_cards:
            return 10  # royal flush
        scv= sorted([card_value(card) for card in cards])
        if scv[1]==scv[0]+1 and scv[2]==scv[1]+1 and scv[3]==scv[2]+1 and scv[4]==scv[3]+1 and len(unique_suites) == 1:
            return 9 # straight flush
        if len(unique_suites) == 1:
            return 6 # flush
        if scv[1]==scv[0]+1 and scv[2]==scv[1]+1 and scv[3]==scv[2]+1 and scv[4]==scv[3]+1:
            return 5 # straight
        return 1  # high card
    elif len(unique_cards) == 4: # one pair
        for card in unique_cards:
            if cards.count(card) == 2:
                return 2
    elif len(unique_cards) == 3: # two pairs, three of a kind
        num_pairs = 0
        for card in unique_cards:
            if cards.count(card) == 3:
                return 4 # three of a kind
            elif cards.count(card) == 2:
                num_pairs += 1
            if num_pairs == 2:
                return 3 # two pairs
    elif len(unique_cards) == 2: # four of a kind, full house
        has_three, has_pair = False, False
        for card in unique_cards:
            if cards.count(card) == 4:
                return 8, card_value(card) # four of a kind
            elif cards.count(card) == 3:
                has_three = True
            elif cards.count(card) == 2:
                has_pair = True
            if has_three and has_pair:
                return 7  # full house

num1wins = 0
for line in poker:
    b1 = hand_value(line, 1)
    b2 = hand_value(line, 2)
    if b1 > b2:
        num1wins += 1
    elif b2 > b1:
        pass
    else:
        t1, t2 = tie_break(line, 1), tie_break(line, 2)
        for idx in range(min(len(t1), len(t2))):
            if t1[idx] > t2[idx]:
                num1wins += 1
                break
            elif t2[idx] > t1[idx]:
                break
print(num1wins)
