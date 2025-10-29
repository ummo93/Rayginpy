from pyray import Vector2, Texture, draw_texture_ex, WHITE, vector2_subtract

from app.core.actor import Actor


class TexturedActor(Actor):
    def __init__(self, texture: Texture, scale: float = 1.0, position=Vector2(0, 0), rotation=Vector2(0, 0)):
        super().__init__()
        self.texture = texture
        self.scale = scale

    def get_scale(self):
        return Vector2(self.texture.width, self.texture.height)

    def on_draw(self):
        draw_texture_ex(
            self.texture,
            vector2_subtract(self.position, Vector2((self.texture.width*self.scale)/2, (self.texture.height*self.scale)/2)),
            self.rotation.x,
            self.scale,
            WHITE
        )