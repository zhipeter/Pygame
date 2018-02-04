'''
This is a game stat
'''


class GameStats():
    '''follow game status'''

    def __init__(self, set):
        '''init info'''
        self.set = set
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        '''reset info'''
        self.ships_left = self.set.ship_limit
        self.score = 0
        self.level = 1
