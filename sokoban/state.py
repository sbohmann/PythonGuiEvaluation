from collections import namedtuple

class State:
    def __init__(self, map, player_position, crate_positions):
        self._map = map
        self._player_position = player_position
        self._crate_positions = set(crate_positions)

    @property
    def player_position(self):
        return self._player_position

    @property
    def crate_positions(self):
        return self._crate_positions

    def move(self, dx, dy):
        x, y = self._player_position
        new_x, new_y = x + dx, y + dy
        if not self._map.accessible(new_x, new_y):
            return False
        if not self._clear_path(new_x, new_y, dx, dy):
            return False
        self._player_position = new_x, new_y
        return True

    def _clear_path(self, x, y, dx, dy):
        if (x, y) in self._crate_positions:
            return self._move_crate(x, y, dx, dy)
        else:
            return True

    def _move_crate(self, crate_x, crate_y, dx, dy):
        previous_crate_position = (crate_x, crate_y)
        self._check_crate_position(previous_crate_position)
        new_crate_position = crate_x + dx, crate_y + dy
        return self._move_crate_if_possible(previous_crate_position, new_crate_position)

    def _move_crate_if_possible(self, previous_crate_position, new_crate_position):
        if self._position_accessible_for_crate(new_crate_position):
            self._replace_crate_position(previous_crate_position, new_crate_position)
            return True
        else:
            return False

    def _replace_crate_position(self, previous_crate_position, new_crate_position):
        self._crate_positions.remove(previous_crate_position)
        self._crate_positions.add(new_crate_position)

    def _position_accessible_for_crate(self, position):
        x, y = position
        return self._map.accessible(x, y) and (position not in self._crate_positions)

    def _check_crate_position(self, position):
        if position not in self._crate_positions:
            raise ValueError
