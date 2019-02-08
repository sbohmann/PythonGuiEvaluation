from state import State

class Map:
    def __init__(self, name, width, height, fields, player_position, crate_positions):
        self._check_size(width, height, fields)
        self.name = name
        self.width = width
        self.height = height
        self.fields = fields
        self._initial_player_position = player_position
        self._initial_crate_positions = crate_positions

    def _check_size(self, width, height, fields):
        if len(fields) != width * height:
            raise ValueError()

    def __getitem__(self, coordinates):
        x, y = coordinates
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            raise ValueError()
        return self.fields[y * self.width + x]

    def accessible(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        else:
            return self.fields[y * self.width + x].accessible

    def create_initial_state(self):
        return State(self._initial_player_position, self._initial_crate_positions)
