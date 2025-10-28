from pyray import *

from app.core.node import Node

class Star(Node):
    def __init__(self, width: int, gravity: float, color: Color = RED):
        super().__init__()
        self.width = width
        self.gravity = gravity
        self.color = color

    def render(self, delta: float):
        draw_circle(int(self.position.x), int(self.position.y), self.width, self.color)