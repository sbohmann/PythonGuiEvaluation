import math
from kivy.graphics.instructions import InstructionGroup
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics.context_instructions import Translate, Scale


class GamePanel(Widget):
    def __init__(self, map):
        super().__init__()
        self.grid_size = 10
        self.field_size = 50
        self.bind(pos=(lambda x, y: self.paint()), size=(lambda width, height: self.paint()))

    def paint(self):
        self.canvas.clear()
        self.canvas.add(Translate(0, self.height))
        self.canvas.add(Scale(1, -1, -1))

        self._paint_grid()

        blue = InstructionGroup()
        blue.add(Color(0, 0, 1, 0.2))
        blue.add(Rectangle(pos=self.pos, size=(100, 100)))
        green = InstructionGroup()
        green.add(Color(0, 1, 0, 0.4))
        green.add(Rectangle(pos=(100, 100), size=(100, 100)))
        [self.canvas.add(group) for group in [blue, green]]

    def _paint_grid(self):
        for y in range(0, math.ceil(self.height), math.ceil(self.grid_size)):
            for x in range(0, math.ceil(self.width), math.ceil(self.grid_size)):
                self._paint_grid_square(x, y)

    def _paint_grid_square(self, x, y):
        self.canvas.add(self._grid_square_color(x, y))
        self.canvas.add(self._grid_square_rectangle(x, y))

    def _grid_square_rectangle(self, x, y):
        return Rectangle(pos=(x, y), size=(self.grid_size, self.grid_size))

    def _grid_square_color(self, x, y):
        return Color(0.7, 0.7, 0.7, 1) if (x + y) % 20 == 0 else Color(0.9, 0.9, 0.9, 1)