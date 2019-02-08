from kivy.uix.gridlayout import GridLayout


class MainPanel:
    def __init__(self, map):
        self._create_view(map)
        self._init_view()

    def _create_view(self, game_panel):
        self.view = GridLayout()
        self._game_panel = game_panel

    def _init_view(self):
        self.view.rows = 1
        self.view.cols = 1
        self.view.add_widget(self._game_panel)