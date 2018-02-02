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

    def reset_stats(self):
        '''reset info'''
        self.ships_left = self.set.ship_limit
