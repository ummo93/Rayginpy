from app.core.actor import Actor
from pyray import RAYWHITE, Camera2D
import types


class Scene:
    def __init__(self):
        self.actors = []
        self.to_destroy = []
        self.camera: Camera2D|None = None
        self.name = self.__class__.__name__

    # Lifecycle methods
    def on_init(self):
        pass

    def on_update(self, dt):
        pass

    def draw_on_background(self):
        pass

    def on_draw(self):
        pass

    def before_draw(self):
        pass

    def on_destroy(self):
        pass

    def on_end_frame(self):
        if not self.to_destroy:
            return
        actor = self.to_destroy.pop(0)
        actor.on_destroy()
        actor.scene = None
        self.actors.remove(actor)

    def find(self, predicate: types.FunctionType) -> Actor|None:
        for actor in self.actors:
            if predicate(actor):
                return actor
        return None

    # Core methods
    def draw_hierarchy(self):
        for actor in self.actors:
            actor.on_draw()

    def update_hierarchy(self, dt):
        for actor in self.actors:
            actor.on_update(dt)
        for actor in self.actors:
            actor.on_update_physic(dt)

    def spawn(self, actor):
        self.actors.append(actor)
        actor.scene = self
        actor.on_init()

    def remove(self, actor):
        self.to_destroy.append(actor)

    def remove_all(self):
        self.to_destroy.extend(self.actors)

    def get_camera(self):
        return self.camera

    def add_camera(self, camera2d):
        self.camera = camera2d

    def get_background_color(self):
        return RAYWHITE
