from copy import deepcopy
import numpy as np

from dealer import BelkaDealer as Dealer
from player import BelkaPlayer as Player
from round import BelkaRound as Round

class BelkaGame(object):
    def __init__(self, allow_step_back=False):
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()
        self.num_players = 4
        self.payoffs = [0 for _ in range (self.num_players)]
        self.scores = [0, 0]
        

    def init_game(self):
        self.payoffs = [0 for _ in range(self.num_players)]
        self.scores = [0, 0]

        self.dealer = Dealer(self.np_random)
        self.players = [Player(i, self.np_random) for i in range(self.num_players)]
        for player in self.players:
            self.dealer.deal_cards(player, 8)
        
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

    def get_current_hand(self):
        return self.round.get_current_hand(self.players, self.round.current_player)

    def get_legal_actions(self):
        return self.round.get_legal_actions(self.players, self.round.current_player)
        
    def get_state(self, player_id):
        state = self.round.get_state(self.players, player_id)

    def get_payoffs(self):
        return self.scores
    
    def count_round(self):
        points = self.round.count_cards_in_play()
        winner = self.round.get_winner()
        self.scores[winner] += points
        self.round.cards_in_play = []
        self.round.first_card = None

if __name__ == '__main__':
    #import time
    #random.seed(0)
    #start = time.time()
    game = BelkaGame()
    for _ in range(2):
        i = 0
        state, button = game.init_game()
        print(button, state)
        for _ in range(8):
            i += 1
            for _ in range(4):
                current_hand = game.get_current_hand()
                print('current_hand', current_hand)
                legal_actions = game.get_legal_actions()
                print('legal_actions', legal_actions)
                action = np.random.choice(legal_actions)
                print('action', action)
                print()
                state, button = game.step(action)
                print(button, state)
            game.count_round()
            print(game.scores)
        print(game.get_payoffs())
        print('~~~~~~~~~~~~~~~~~~~~~~')
    print('step', i)