from copy import deepcopy
import numpy as np

import BelkaDealer as Dealer
import BelkaPlayer as Player
import BelkaRound as Round

class BelkaGame(object):
    def __init__(self):
        self.np_random = np.random.RandomState()
        self.num_players = 2

    def init_game(self):
        self.dealer = Dealer(self.np_random)
        self.players = [Player(i, self.np_random) for i in range(self.num_players)]
        for player in self.players:
            self.dealer.deal_cards(player, 8)
        
        self.trump_suit = get_trump_suit(players)
        
        self.round = Round(self.dealer, self.num_players, self)

        self.history = []

        player_id = self.round.current_player
        state = self.get_state(player_id)

        return state, player_id

    def get_legal_actions(self):
        return self.round.get_legal_actions(self.players, self.round.current_player, self.trump_suit)


    def get_trump_suit(self, players):


