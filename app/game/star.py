from pyray import Color, RED, load_texture, get_mouse_position, is_mouse_button_pressed, is_mouse_button_down, \
    vector2_distance, get_world_to_screen_2d, get_screen_to_world_2d, is_mouse_button_up

from app.core.textured_actor import TexturedActor


class Star(TexturedActor):
    is_drag = False
    def __init__(self, width: int, color: Color = RED):
        super().__init__(load_texture("assets/star.png"), 0.25, color)
        self.width = width
        self.color = color

    def on_update(self, dt: float):
        mouse_pos = get_mouse_position()
        if is_mouse_button_down(0) and vector2_distance(mouse_pos, get_world_to_screen_2d(self.position, self.scene.camera)) < self.width * 2:
            self.is_drag = True

        if is_mouse_button_up(0):
            self.is_drag = False

        if self.is_drag:
            self.set_position(get_screen_to_world_2d(mouse_pos, self.scene.camera))