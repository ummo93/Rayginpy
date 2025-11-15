from app.core.scene import Scene
from pyray import Vector2, BLACK, WHITE, Camera2D, draw_text, vector2_distance, get_screen_width, get_screen_height

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
        self.player.velocity = Vector2(-4, 0)
        self.spawn(self.star)
        self.spawn(self.player)

        camera = Camera2D()
        camera.zoom = 1.5

        self.add_camera(camera)

    def get_background_color(self):
        return BLACK

    def on_draw(self):
        draw_text("Gravity", 10, 10, 21, WHITE)

    def on_update(self, dt):
        self.camera.target = self.star.position
        self.camera.offset = Vector2(get_screen_width()/2, get_screen_height()/2)
        if vector2_distance(self.player.position, self.player.gravity_center) < 15:
            self.remove(self.player)
            self.remove(self.star)
            self.on_init()
