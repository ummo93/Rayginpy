from pyray import BLACK, Vector2, YELLOW, draw_text
from raylib.colors import WHITE

from app.core.scene import Scene
from app.model.player import Player
from app.model.star import Star


class MainScene(Scene):
    def __init__(self):
        super().__init__("Main scene", BLACK)
        self.before_init()

    def before_init(self):
        star = Star(15, 0.1, YELLOW)
        star.set_pos(Vector2(500, 300))

        player = Player(8, 0.25)
        player.set_pos(Vector2(200, 200))

        self.add_child(player)
        self.add_child(star)

    def render(self):
        super().render()
        draw_text("Gravity", 10, 10, 21, WHITE)
