import random

from app.core.scene import Scene
from pyray import Vector2, BLACK, WHITE, ORANGE, Camera2D, draw_text, vector2_distance, get_screen_width, \
    get_screen_height, get_world_to_screen_2d, load_texture

from app.core.textured_actor import TexturedActor
from app.core.utils import midpoint
from app.game.player import Player
from app.game.star import Star


class MainScene(Scene):
    star = None
    star2 = None
    player = None
    background = None

    star_pos_on_init = Vector2(350, 350)
    star2_pos_on_init = Vector2(800, 400)

    def __init__(self):
        super().__init__()

    def on_init(self):
        self.star = Star(15, WHITE)
        self.star2 = Star(15, WHITE)
        self.player = Player(4, 25)
        self.star.set_position(self.star_pos_on_init)
        self.star2.set_position(self.star2_pos_on_init)

        mid = midpoint(self.star.position, self.star2.position)

        if vector2_distance(mid, self.star.position) < 10:
            self.player.set_position(Vector2(mid.x + random.randrange(-200, 200), mid.y + random.randrange(-200, 200)))
        else:
            self.player.set_position(Vector2(mid.x, mid.y))

        self.background = TexturedActor(load_texture("assets/background.png"), 0.4, ORANGE, Vector2(mid.x, mid.y), Vector2(0, 0))

        camera = Camera2D()
        camera.zoom = 1.5

        self.add_camera(camera)
        self.spawn(self.star)
        self.spawn(self.star2)
        self.spawn(self.player)
        self.spawn(self.background)

        self.player.velocity = Vector2(random.randrange(-3, -6, -1), 0)

    def get_background_color(self):
        return BLACK

    def on_draw(self):
        draw_text("Gravity", 10, 10, 21, WHITE)

    def on_update(self, dt: float):
        mid = midpoint(self.star.position, self.star2.position)
        self.camera.target = mid
        mid_screen = get_world_to_screen_2d(mid, self.camera)
        draw_text("x", int(mid_screen.x), int(mid_screen.y), 25, WHITE)
        self.camera.offset = Vector2(get_screen_width()/2, get_screen_height()/2)
        if self.is_game_over:
            self.star_pos_on_init = self.star.position
            self.star2_pos_on_init = self.star2.position
            self.remove_all()
            self.on_init()

    @property
    def is_game_over(self) -> bool:
        fall_star = self.find_all(lambda actor: isinstance(actor, Star) and vector2_distance(actor.position, self.player.position) < 15)
        if len(fall_star) > 0:
            return True

        if self.camera is None:
            return False

        screen_pos = get_world_to_screen_2d(self.player.position, self.camera)

        return (
            screen_pos.x < 0 or
            screen_pos.x > get_screen_width() or
            screen_pos.y < 0 or
            screen_pos.y > get_screen_height()
        )