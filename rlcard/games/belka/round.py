import Card

class BelkaRound(object):
    def __init__(self, dealer, num_players, np_random):
        self.np_random = np_random
        self.dealer = dealer

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

    