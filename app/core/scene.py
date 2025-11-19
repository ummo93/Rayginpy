from typing import Callable

from app.core.actor import Actor
from pyray import RAYWHITE, Camera2D

class Scene:
    def __iter__(self):
        return iter(self.actors)

    def __init__(self):
        self.actors = []
        self.to_destroy = []
        self.camera: Camera2D|None = None
        self.name = self.__class__.__name__

    # Lifecycle methods
    def on_init(self):
        pass

    def on_update(self, dt: float):
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

    def find(self, predicate: Callable[[Actor], bool]) -> Actor|None:
        for actor in self.actors:
            if predicate(actor):
                return actor
        return None

    def find_all(self, predicate: Callable[[Actor], bool]) -> list[Actor]:
        return [actor for actor in self.actors if predicate(actor)]

    # Core methods
    def draw_hierarchy(self):
        for actor in self.actors:
            actor.on_draw()

    def update_hierarchy(self, dt: float):
        for actor in self.actors:
            actor.on_update(dt)
        for actor in self.actors:
            actor.on_update_physic(dt)

    def spawn(self, actor: Actor):
        self.actors.append(actor)
        actor.scene = self
        actor.on_init()

    def remove(self, actor: Actor):
        self.to_destroy.append(actor)

    def remove_all(self):
        self.to_destroy.extend(self.actors)

    def get_camera(self):
        return self.camera

    def add_camera(self, camera2d: Camera2D):
        self.camera = camera2d

    def get_background_color(self):
        return RAYWHITE
