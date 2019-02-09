import itertools
from map import Map
from field import Field


class MapFromLines:
    def __init__(self, name, lines):
        self._name = name
        self._lines = lines
        self._player_position = None
        self._crate_positions = []
        self._create_result(name)

    def _create_result(self, name):
        self._process_lines()
        self._create_fields()
        self.result = Map(name, self._width, self._height, self._fields, self._player_position, self._crate_positions)

    def _process_lines(self):
        self._width = max(map(len, self._lines))
        self._height = len(self._lines)
        self._keys = [None] * self._width * self._height
        for line, offset in zip(self._lines, range(0, self._height)):
            self._parse_line(line, offset)

    def _parse_line(self, line, y):
        offset = y * self._width
        started = False
        for key, x in zip(line, itertools.count()):
            if started or key != ' ':
                filtered_key = self._filter_key(key, y)
                self._keys[offset + x] = filtered_key
                started = True
            self._process_key(x, y, key)

    def _filter_key(self, key, y):
        return None if self._first_or_last_line(y) and key == ' ' else key

    def _first_or_last_line(self, y):
        first_line = (y == 0)
        last_line = (y == len(self._lines) - 1)
        return first_line or last_line

    def _process_key(self, x, y, key):
        if key == '@' or key == '+':
            self._set_player_position(x, y)
        elif key == '$' or key == '*':
            self._crate_positions.append((x, y))

    def _set_player_position(self, x, y):
        if self._player_position != None:
            raise ValueError('Double player position')
        self._player_position = (x, y)

    def _create_fields(self):
        self._fields = list(map(Field, self._keys))
