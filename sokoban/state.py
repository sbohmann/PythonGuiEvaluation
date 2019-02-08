from collections import namedtuple

class State:
    def __init__(self, player_position, crate_positions):
        self.player_position = player_position
        self.crate_positions = crate_positions
