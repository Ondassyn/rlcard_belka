class BelkaPlayer(object):
    def __init__(self, player_id, np_random):
        self.np_random = np_random
        self.player_id = player_id
        self.hand = []
        self.stack = []

    def get_player_id(self):
        return self.player_id