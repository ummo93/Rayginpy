from pyray import Color, RED, draw_circle

from app.core.actor import Actor


class Star(Actor):
    def __init__(self, width: int, gravity: float, color: Color = RED):
        super().__init__()
        self.width = width
        self.gravity = gravity
        self.color = color

    def on_draw(self):
        draw_circle(int(self.position.x), int(self.position.y), self.width, self.color)