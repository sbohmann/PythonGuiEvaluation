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
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode[1])
        direction = None
        if keycode[1] == 'left':
            direction = (-1, 0)
        elif keycode[1] == 'right':
            direction = (1, 0)
        elif keycode[1] == 'up':
            direction = (0, -1)
        elif keycode[1] == 'down':
            direction = (0, 1)
        self._move(direction)
        return True

    def build(self):
        return self._mainPanel.view

    def _move(self, direction):
        dx, dy = direction
        x, y = _move(self._state.player_position, dx, dy)
        if self._map.accessible(x, y):
            # crate
            # if self._crate_for_position
            self._state.player_position = (x, y)
            self._game_panel.paint()


def _move(position, dx, dy):
    x, y = position
    return (x + dx, y + dy)

Sokoban().run()
