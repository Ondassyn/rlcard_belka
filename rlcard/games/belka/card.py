class Card(object):
    suit = None
    rank = None

    valid_suit = ['C', 'S', 'H', 'D']
    valid_rank = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit
        self.rank

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        else:
            return NotImplemented

    def __hash__(self):
        suit_index = Card.valid_suit.index(self.suit)
        rank_index = Card.valid_rank.index(self.rank)
        return rank_index + 100 * suit_index

    def __str__(self):
        return self.rank + self.suit

    def get_index(self):
        return self.suit+self.rank