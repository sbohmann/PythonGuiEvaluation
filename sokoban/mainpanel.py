from kivy.uix.gridlayout import GridLayout


class MainPanel:
    def __init__(self):
        self._game_panel = None
        self._create_view()
        self._init_view()

    def set_game_panel(self, _game_panel):
        self._remove_existing_game_panel()
        self._game_panel = _game_panel
        self.view.add_widget(self._game_panel)

    def _remove_existing_game_panel(self):
        if self._game_panel:
            self.view.remove_widget(self._game_panel)

    def _create_view(self):
        self.view = GridLayout()

    def _init_view(self):
        self.view.rows = 1
        self.view.cols = 1