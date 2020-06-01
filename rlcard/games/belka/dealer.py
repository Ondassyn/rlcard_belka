from rlcard.utils import init_standard_deck
import numpy as numpy

class BelkaDealer(object):
    def __init__(self, np_random):
        self.np_random = np_random
        self.deck = init_deck()
        self.shuffle()

    def shuffle(self):
        self.np_random.shuffle(self.deck)

    def deal_cards(self, player, num):
        for _ in range(num):
            player.hand.append(self.deck.pop())