from raylib.defines import GLFW_KEY_W, GLFW_KEY_D, GLFW_KEY_A, GLFW_KEY_S

from app.core.actor import Actor
from pyray import RED, GRAY, Vector2, is_key_down, vector2_normalize, vector2_scale, vector2_add, \
    vector2_subtract, draw_circle_v, vector2_distance_sqr, Color

from app.core.utils import draw_lines_batch
from app.game.star import Star


class Player(Actor):
    trajectory: list[tuple[float, float]] = []
    orbit_color: Color = Color(GRAY[0], GRAY[1], GRAY[2], GRAY[3])

    def __init__(self, width, speed):
        super().__init__()
        self.width = width
        self.speed = speed
        self.velocity = Vector2(0, 0)
        self.gravity_center = Vector2(0, 0)


    def on_init(self):
        star = self.scene.find(lambda node: isinstance(node, Star))
        self.gravity_center = star.position
        self.trajectory.clear()

    def on_update(self, delta: float):
        move_vector = Vector2(0, 0)
        if is_key_down(GLFW_KEY_W):
            move_vector.y = -self.speed
        if is_key_down(GLFW_KEY_S):
            move_vector.y = self.speed
        if is_key_down(GLFW_KEY_A):
            move_vector.x = -self.speed
        if is_key_down(GLFW_KEY_D):
            move_vector.x = self.speed

        heading = vector2_normalize(vector2_subtract(self.gravity_center, self.position))
        distance_sqr = vector2_distance_sqr(self.gravity_center, self.position)

        gravity = vector2_scale(heading, 1/distance_sqr)
        self.velocity = vector2_add(self.velocity, vector2_scale(gravity, delta*1e5))
        self.velocity = vector2_add(self.velocity, vector2_scale(move_vector, delta))

        # restriction on max speed
        self.position = vector2_add(self.position, self.velocity)

        if len(Player.trajectory) > 100:
            Player.trajectory.pop(0)

        Player.trajectory.append((self.position.x, self.position.y))


    def on_draw(self):
        draw_circle_v(self.position, self.width, RED)
        draw_lines_batch(Player.trajectory, self.orbit_color, True, 5, 2)
