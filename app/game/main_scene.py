from app.core.scene import Scene
from pyray import Vector2, BLACK, WHITE, Camera2D, draw_text, vector2_distance

from app.game.player import Player
from app.game.star import Star


class MainScene(Scene):
    star = None
    player = None

    def __init__(self):
        super().__init__()

    def on_init(self):
        self.star = Star(15, WHITE)
        self.player = Player(4, 15)
        self.star.set_position(Vector2(350, 350))
        self.player.set_position(Vector2(350, 450))
        self.player.velocity = Vector2(-1, 0)
        self.spawn(self.star)
        self.spawn(self.player)

        camera = Camera2D()
        camera.target = self.star.position
        camera.offset = Vector2(400, 300)
        camera.zoom = 1.5

        self.add_camera(camera)

    def get_background_color(self):
        return BLACK

    def on_draw(self):
        draw_text("Gravity", 10, 10, 21, WHITE)

    def on_update(self, dt):
        if vector2_distance(self.player.position, self.player.gravity_center) < 15:
            self.remove(self.player)
            self.remove(self.star)
            self.on_init()
