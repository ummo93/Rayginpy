from pyray import Vector2


class Node:
    def __init__(self):
        self.current_scene = None
        self.position = Vector2(0,0)

    def _set_scene(self, current_scene):
        self.current_scene = current_scene

    def set_pos(self, pos: Vector2):
        self.position = pos

    def render(self, delta: float):
        pass

    def ready(self):
        pass
