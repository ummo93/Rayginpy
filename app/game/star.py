from pyray import Color, RED, load_texture

from app.core.textured_actor import TexturedActor


class Star(TexturedActor):
    def __init__(self, width: int, gravity: float, color: Color = RED):
        super().__init__(load_texture("./app/assets/star.png"), 0.25, color)
        self.width = width
        self.gravity = gravity
        self.color = color