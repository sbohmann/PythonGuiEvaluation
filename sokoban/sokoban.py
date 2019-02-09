from threading import Timer

from kivy.app import App
from kivy.core.window import Window

from mainpanel import MainPanel
from gamepanel import GamePanel
from maps_from_file import MapsFromFile


class Sokoban(App):
    def __init__(self):
        super().__init__()
        self._map = MapsFromFile('100Boxes.txt').result[0]
        self._state = self._map.create_initial_state()
        self._game_panel = GamePanel(self._map, self._state)
        self._mainPanel = MainPanel(self._game_panel)
        self.setup_keyboard_handling()

    def setup_keyboard_handling(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self._game_panel)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        direction = _direction_for_keycode.get(keycode[1], None)
        if direction is not None:
            self._move(direction)
        if keycode[1] == 'escape':
            self._state = self._map.create_initial_state()
            self._game_panel.set_state(self._state)
        return True

    def build(self):
        return self._mainPanel.view

    def _move(self, direction):
        dx, dy = direction
        if self._state.move(dx, dy):
            self._game_panel.paint()


def _move(position, dx, dy):
    x, y = position
    return (x + dx, y + dy)


_direction_for_keycode = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1)
}

Sokoban().run()
