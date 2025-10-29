from app.core.scene import Scene
from pyray import Vector2, YELLOW, BLACK, WHITE, Camera2D, draw_text, vector2_distance

from app.game.player import Player
from app.game.star import Star


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.star = None
        self.player = None

    def on_init(self):
        self.star = Star(15, 5, YELLOW)
        self.player = Player(8, 5)
        self.player.velocity = Vector2(0, -5)
        self.star.set_position(Vector2(350, 350))
        self.player.set_position(Vector2(200, 350))

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
