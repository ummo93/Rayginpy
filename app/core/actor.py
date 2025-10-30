from pyray import Vector2, vector2_add
from math import cos, sin, radians


class Actor:
    __id_counter = 0

    def __init__(self, position=Vector2(0, 0), rotation=Vector2(0, 0)):
        Actor.__id_counter += 1
        self.id = Actor.__id_counter
        self.position = position
        self.rotation = rotation
        self.collider = None
        self.scene = None
        self.destructed = False
        self._last_pos = Vector2(position.x, position.y)

    def get_forward(self):
        return Vector2(sin(radians(self.rotation.y)), -cos(radians(self.rotation.y)))

    def get_right(self):
        return Vector2(cos(radians(self.rotation.y)), sin(radians(self.rotation.y)))

    def set_position(self, new_pos):
        self._last_pos = self.position
        self.position = new_pos

    # Lifecycle
    def on_init(self): pass
    def on_update(self, dt): pass
    def on_draw(self): pass

    def on_destroy(self):
        self.destructed = True

    def on_update_physic(self, dt):
        if not self.collider:
            return
        offset = Vector2(self.position.x - self._last_pos.x, self.position.y - self._last_pos.y)
        self.collider.min = vector2_add(self.collider.min, offset)
        self.collider.max = vector2_add(self.collider.max, offset)
