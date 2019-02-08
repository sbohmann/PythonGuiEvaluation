from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from gamepanel import GamePanel

class Sokoban(App):
    def __init__(self):
        super().__init__()
        self.mainPanel = MainPanel()

    def build(self):
        return self.mainPanel.view


class MainPanel:
    def __init__(self):
        self._create_view()
        self._init_view()

    def _create_view(self):
        self.view = GridLayout()
        self._game_panel = GamePanel(None)

    def _init_view(self):
        self.view.rows = 1
        self.view.cols = 1
        self.view.add_widget(self._game_panel)


Sokoban().run()
