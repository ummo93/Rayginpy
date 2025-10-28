from pyray import *
from typing import Callable

from app.core.node import Node


class Scene:
    def __init__(self, name: str, background: Color = WHITE):
        self.nodes: list[Node] = []
        self.name = name
        self.background = background
        self.restart = False

    def find(self, foo: Callable[[Node], bool]) -> Node|None:
        for node in self.nodes:
            if foo(node):
                return node
        return None

    def add_child(self, obj: Node):
        obj._set_scene(self)
        self.nodes.append(obj)

    def render(self):
        begin_drawing()
        delta = get_frame_time()
        clear_background(self.background)
        for i, obj in enumerate(self.nodes):
            obj.render(delta)
        end_drawing()

    def ready(self):
        for i, obj in enumerate(self.nodes):
            obj.ready()

    def restart_scene(self):
        self.restart = True
