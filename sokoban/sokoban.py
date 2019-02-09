from threading import Timer

from kivy.app import App
from kivy.core.window import Window

from mainpanel import MainPanel
from gamepanel import GamePanel
from maps_from_file import MapsFromFile


class Sokoban(App):
    def __init__(self):
        super().__init__()
        self._read_maps()
        self._setup_state()
        self._setup_ui()

    def build(self):
        return self._mainPanel.view

    def _setup_state(self):
        self._state = self._map.create_initial_state()

    def _read_maps(self):
        self._maps = MapsFromFile('100Boxes.txt').result
        self._map_index = 0
        self._map = self._maps[self._map_index]
        self._set_window_title()

    def _setup_ui(self):
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
        print(keycode)
        direction = _direction_for_keycode.get(keycode[1], None)
        if direction is not None:
            self._move(direction)
        elif keycode[1] == 'escape':
            self._reset_state()
        elif keycode[1] == 'pageup':
            self._switch_map(1)
        elif keycode[1] == 'pagedown':
            self._switch_map(-1)
        return True

    def _reset_state(self):
        self._state = self._map.create_initial_state()
        self._game_panel.set_state(self._state)

    def _move(self, direction):
        dx, dy = direction
        if self._state.move(dx, dy):
            self._game_panel.paint()

    def _switch_map(self, delta):
        self._map_index = (self._map_index + delta) % len(self._maps)
        if self._map_index < 0:
            self._map_index += len(self._maps)
        self._map = self._maps[self._map_index]
        self._state = self._map.create_initial_state()
        self._game_panel = GamePanel(self._map, self._state)
        self._mainPanel.set_game_panel(self._game_panel)
        self._set_window_title()

    def _set_window_title(self):
        self.title = 'Sokobal Level ' + str(self._map_index + 1)


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
