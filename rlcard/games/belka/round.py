import Card

class BelkaRound(object):
    def __init__(self, dealer, num_players, np_random):
        self.np_random = np_random
        self.dealer = dealer
        self.first_card = None
        self.current_player = 0
        self.num_players = 4
        self.played_cards = []
        self.winner = None

    def get_legal_actions(self, players, player_id, trump_suit):
        legal_actions = []
        hand = players[player_id].hand
        first_card = self.first_card
        
        if first_card.suit != trump_suit and first_card.rank != 'J':
            for card in hand:
                if card.suit == first_card:
                    legal_actions.append(card.str)

        if legal_actions:
            return legal_actions

        if first_card.suit == trump_suit or first_card.rank == 'J':
            for card in hand:
                if card.suit == trump_suit or card.rank == 'J':
                    legal_actions.append(card.str)
        
        if legal_actions:
            return legal_actions
        
        for card in hand:
            legal_actions.append(card.str)

        return legal_actions

    def proceed_round(self, players, action):
        player = players[self.current_player]
        card_info = action.split('-')
        rank = card_info[0]
        suit = card_info[1]

        remove_index = None
        for index, card in enumerate(player.hand):
            if rank == card.rank and suit == card.suit:
                remove_index = index

        card = player.hand.pop(remove_index)
        self.played_cards.append(card)

    def get_state(self, players, player_id):
        state = {}
        player = players[player_id]
        state['hand'] = cards2list(player.hand)
        state['target'] = self.target.str
    