from card import Card
from utils import cards2list

class BelkaRound(object):
    def __init__(self, dealer, num_players, np_random):
        self.np_random = np_random
        self.dealer = dealer
        self.first_card = None
        self.cards_in_play = []
        self.current_player = 0
        self.num_players = 4
        self.played_cards = []
        self.trump_suit = self.set_trump_suit()
        self.winner = -1
        self.player_suit = []

    def get_current_hand(self, players, player_id):
        hand = []
        for card in players[player_id].hand:
            hand.append(card.__str__())
        return hand

    def set_trump_suit(self, players):
        if not self.player_suit:
            self.trump_suit = 'C'
        else:
            for i in range(self.num_players):
                for card in players[i].hand:
                    if card.__str__() == 'JC':
                        self.trump_suit = self.player_suit[i]


    def get_legal_actions(self, players, player_id):
        legal_actions = []
        hand = players[player_id].hand
        if self.first_card == None:
            for card in hand:
                legal_actions.append(card.__str__())
            return legal_actions

        first_card = self.first_card

        if first_card.suit != self.trump_suit and first_card.rank != 'J':
            for card in hand:
                if card.suit == first_card.suit and card.rank != 'J':
                    legal_actions.append(card.str)

        if legal_actions:
            return legal_actions

        if first_card.suit == self.trump_suit or first_card.rank == 'J':
            for card in hand:
                if card.suit == self.trump_suit or card.rank == 'J':
                    legal_actions.append(card.str)
        
        if legal_actions:
            return legal_actions
        
        for card in hand:
            legal_actions.append(card.str)

        return legal_actions

    def proceed_round(self, players, action):
        player = players[self.current_player]
        card_info = action.__str__()
        rank = card_info[0]
        suit = card_info[1]

        remove_index = None
        for index, card in enumerate(player.hand):
            if rank == card.rank and suit == card.suit:
                remove_index = index

        card = player.hand.pop(remove_index)
        if not self.cards_in_play:
            self.first_card = card
        self.cards_in_play.append(card)
        self.played_cards.append(card)

        self.current_player = (self.current_player + 1) % self.num_players

    def get_state(self, players, player_id):
        state = {}
        player = players[player_id]
        state['hand'] = cards2list(player.hand)
        state['cards_in_play'] = cards2list(self.cards_in_play)
        state['played_cards'] = cards2list(self.played_cards)
        others_hand = []
        for player in players:
            if player.player_id != player_id:
                others_hand.extend(player.hand)
        state['others_hand'] = cards2list(others_hand)
        state['legal_actions'] = self.get_legal_actions(players, player_id)
        
        return state

    def count_cards_in_play(self):
        points = 0
        for card in self.cards_in_play:
            if card.rank == 'J':
                points += 2
            elif card.rank == 'Q':
                points += 3
            elif card.rank == 'K':
                points += 4
            elif card.rank == 'A':
                points += 11
            elif card.rank == 'T':
                points += 10
        return points

    def get_winner(self):
        jacks = []
        trumps = []
        legals = []
        for card in self.cards_in_play:
            if card.rank == 'J':
                jacks.append(card)
            if card.suit == self.trump_suit:
                trumps.append(card)
            if card.suit == self.first_card.suit:
                legals.append(card)


        if jacks:
            for card in jacks:
                if card.__str__() == 'JC':
                    return self.cards_in_play.index(card) % 2
            for card in jacks:
                if card.__str__() == 'JS':
                    return self.cards_in_play.index(card) % 2
            for card in jacks:    
                if card.__str__() == 'JH':
                    return self.cards_in_play.index(card) % 2
            return self.cards_in_play.index(jacks[0]) % 2
        
        if trumps:
            max_trump = trumps[0]
            for card in trumps:
                if card > max_trump:
                    max_trump = card
            return self.cards_in_play.index(max_trump) % 2

        max_legal = legals[0]
        for card in legals:
            if card > max_legal:
                max_legal = card
        return self.cards_in_play.index(max_legal) % 2



    