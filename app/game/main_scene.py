import random
from asyncio import sleep

from app.core.scene import Scene
from pyray import Vector2, BLACK, WHITE, ORANGE, Camera2D, draw_text, vector2_distance, get_screen_width, \
    get_screen_height, \
    get_world_to_screen_2d, load_texture, draw_texture, draw_texture_ex

from app.core.textured_actor import TexturedActor
from app.game.player import Player
from app.game.star import Star
import asyncio

class MainScene(Scene):
    star = None
    player = None
    background = None

    def __init__(self):
        super().__init__()

    def on_init(self):
        self.star = Star(15, WHITE)
        self.player = Player(4, 15)
        self.star.set_position(Vector2(350, 350))
        self.player.set_position(Vector2(350, 450))
        self.background = TexturedActor(load_texture("assets/background.png"), 0.4, ORANGE, Vector2(350, 350), Vector2(0, 0))

        camera = Camera2D()
        camera.zoom = 1.5

        self.add_camera(camera)
        self.spawn(self.star)
        self.spawn(self.player)
        self.spawn(self.background)

        self.player.velocity = Vector2(random.randrange(-3, -6, -1), 0)

    def get_background_color(self):
        return BLACK

    def on_draw(self):
        draw_text("Gravity", 10, 10, 21, WHITE)

    def on_update(self, dt):
        self.camera.target = self.star.position
        self.camera.offset = Vector2(get_screen_width()/2, get_screen_height()/2)
        if self.is_game_over:
            self.remove_all()
            self.on_init()

    @property
    def is_game_over(self) -> bool:
        if vector2_distance(self.player.position, self.player.gravity_center) < 15:
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