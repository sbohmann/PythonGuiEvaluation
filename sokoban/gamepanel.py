import math
import random

from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics.context_instructions import Translate, Scale

_grid_size = 10
_field_size = 50

_colors = {
    'wall': lambda: Color(0.3, 0.3, 0.3, 1),
    'floor': lambda: Color(0.7, 0.7, 0.7, 1),
    'target': lambda: Color(0.9, 0.6, 0.6, 1)
}

_player_color = lambda: Color(0.5, 0.5, 0.9, 0.5)
_crate_color = lambda: Color(0.3, 0.2, 0.1, 0.5)


class GamePanel(Widget):
    def __init__(self, map, state):
        super().__init__()
        self._map = map
        self._state = state
        self.bind(pos=(lambda x, y: self.paint()), size=(lambda width, height: self.paint()))

    def set_state(self, state):
        self._state = state
        self.paint()

    def paint(self):
        self._setup_canvas()

        # self._paint_grid()
        self._calculate_map_offset()
        self._paint_map()
        self._paint_state()

    def _setup_canvas(self):
        self.canvas.clear()
        self.canvas.add(Translate(0, self.height))
        self.canvas.add(Scale(1, -1, -1))

    def _paint_grid(self):
        for y in range(0, math.ceil(self.height), math.ceil(_grid_size)):
            for x in range(0, math.ceil(self.width), math.ceil(_grid_size)):
                self._paint_grid_square(x, y)

    def _paint_grid_square(self, x, y):
        self.canvas.add(self._grid_square_color(x, y))
        self.canvas.add(self._grid_square_rectangle(x, y))

    def _grid_square_rectangle(self, x, y):
        return Rectangle(pos=(x, y), size=(_grid_size, _grid_size))

    def _grid_square_color(self, x, y):
        return Color(0.7, 0.7, 0.7, 1) if (x + y) % 20 == 0 else Color(0.9, 0.9, 0.9, 1)

    def _calculate_map_offset(self):
        map_width = self._map.width * _field_size
        map_height = self._map.height * _field_size
        self._map_offset = (
            (self.width - map_width) // 2,
            (self.height - map_height) // 2)

    def _paint_map(self):
        for y in range(0, self._map.height):
            for x in range(0, self._map.width):
                self._paint_field(x, y, self._map[x, y])

    def _paint_field(self, x, y, field):
        if field.image is not None:
            self._paint_field_rectangle(x, y, _colors[field.image])

    def _paint_field_rectangle(self, x, y, color):
        self.canvas.add(color())
        self.canvas.add(Rectangle(
            pos=self._map_position(x, y),
            size=(_field_size, _field_size)))

    def _paint_state(self):
        self._paint_player()
        self._paint_crates()

    def _paint_player(self):
        x, y = self._state.player_position
        self._paint_state_rectangle(x, y, _player_color)

    def _paint_crates(self):
        for crate_position in self._state.crate_positions:
            x, y = crate_position
            self._paint_state_rectangle(x, y, _crate_color)

    def _paint_state_rectangle(self, x, y, color):
        self.canvas.add(color())
        offset = _field_size / 6
        reduced_field_size = _field_size - 2 * offset
        raw_x, raw_y = self._map_position(x, y)
        self.canvas.add(Rectangle(
            pos=(raw_x + offset, raw_y + offset),
            size=(reduced_field_size, reduced_field_size)))

    def _map_position(self, x, y):
        dx, dy = self._map_offset
        return (
            dx + x * _field_size,
            dy + y * _field_size)
