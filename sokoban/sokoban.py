from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics.instructions import InstructionGroup


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
        self._game_panel = GamePanel()

    def _init_view(self):
        self.view.rows = 2
        self.view.cols = 2
        self.view.add_widget(self._game_panel, 4)


class GamePanel(Widget):
    def __init__(self):
        super().__init__()
        self._paint()

    def _paint(self):
        blue = InstructionGroup()
        blue.add(Color(0, 0, 1, 0.2))
        blue.add(Rectangle(pos=self.pos, size=(100, 100)))

        green = InstructionGroup()
        green.add(Color(0, 1, 0, 0.4))
        green.add(Rectangle(pos=(100, 100), size=(100, 100)))

        # Here, self should be a Widget or subclass
        [self.canvas.add(group) for group in [blue, green]]


Sokoban().run()
