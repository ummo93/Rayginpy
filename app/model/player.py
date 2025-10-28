from raylib.defines import GLFW_KEY_W, GLFW_KEY_D, GLFW_KEY_A, GLFW_KEY_S

from app.core.node import Node
from pyray import *

from app.model.star import Star


class Player(Node):
    def __init__(self, width, speed):
        super().__init__()
        self.width = width
        self.speed = speed
        self.velocity = Vector2(0, 0)
        self.gravity_center = Vector2(0, 0)
        self.gravity_value = 0

    def update_position(self):
      self.position = vector2_add(self.position, self.velocity)

    def ready(self):
        star = self.current_scene.find(lambda node: isinstance(node, Star))
        self.gravity_center = star.position
        self.gravity_value = star.gravity

    def render(self, delta: float):
        move_vector = Vector2(0, 0)
        if is_key_down(GLFW_KEY_W):
          move_vector.y = -self.speed * delta
        if is_key_down(GLFW_KEY_S):
          move_vector.y = self.speed * delta
        if is_key_down(GLFW_KEY_A):
          move_vector.x = -self.speed * delta
        if is_key_down(GLFW_KEY_D):
          move_vector.x = self.speed * delta


        gravity = vector2_scale(vector2_normalize(vector2_subtract(self.gravity_center, self.position)), self.gravity_value*delta)
        self.velocity = vector2_add(self.velocity, gravity)
        self.velocity = vector2_add(self.velocity, move_vector)

        # restriction on max speed
        self.velocity = vector2_clamp_value(self.velocity, 0, 0.25)

        self.update_position()
        draw_circle(int(self.position.x), int(self.position.y), self.width, RED)

        if vector2_distance(self.position, self.gravity_center) < 15:
            self.current_scene.restart_scene()