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

    def step(self, action):
        if self.allow_step_back:
            his_dealer = deepcopy(self.dealer)
            his_round = deepcopy(self.round)
            his_players = deepcopy(self.players)
            self.history.append((his_dealer, his_players, his_round))

        self.round.proceed_round(self.players, action)
        player_id = self.round.current_player
        state = self.get_state(player_id)
        return state, player_id

    def get_legal_actions(self):
        return self.round.get_legal_actions(self.players, self.round.current_player, self.trump_suit)


    def get_trump_suit(self, players):
        

if __name__ == '__main__':
    #import time
    #random.seed(0)
    #start = time.time()
    game = BelkaGame()
    for _ in range(1):
        state, button = game.init_game()
        print(button, state)
        for _ in range(8):
            legal_actions = game.get_legal_actions()
            print('legal_actions', legal_actions)
            action = np.random.choice(legal_actions)
            print('action', action)
            print()
            state, button = game.step(action)
            print(button, state)
        print(game.get_payoffs())
    print('step', i)
