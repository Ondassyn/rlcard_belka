from card import Card

def init_deck():
    suit_list = ['C', 'S', 'H', 'D']
    rank_list = ['7', '8', '9', 'J', 'Q', 'K', 'T', 'A']
    deck = [Card(suit, rank) for suit in suit_list for rank in rank_list]
    return deck


def cards2list(cards):
    cards_list = []
    for card in cards:
        cards_list.append(card.__str__)
    return cards_list