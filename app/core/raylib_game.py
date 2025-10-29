from app.core.context import GameContext
from pyray import *

class RaylibGame:
    def __init__(self, settings, scene):
        self.settings = settings
        self.ctx = GameContext()
        self.scene = scene
        self.running = False

    def refresh_context(self):
        self.ctx.window_width = get_screen_width()
        self.ctx.window_height = get_screen_height()
        self.ctx.fps = get_fps()
        self.ctx.delta = get_frame_time()

    def init(self):
        init_window(self.settings.width, self.settings.height, self.settings.title)
        set_window_state(self.settings.window_flags)
        set_target_fps(self.settings.target_fps)
        init_audio_device()
        self.refresh_context()

    def start_game_loop(self):
        self.running = True
        self.scene.on_init()

        while not window_should_close():
            self.refresh_context()
            self.scene.update_hierarchy(self.ctx.delta)
            self.scene.on_update(self.ctx.delta)

            begin_drawing()
            clear_background(self.scene.get_background_color())
            self.scene.draw_on_background()

            camera2d = self.scene.get_camera()
            if camera2d:
                begin_mode_2d(camera2d)

            self.scene.before_draw()
            self.scene.draw_hierarchy()

            if camera2d:
                end_mode_2d()

            self.scene.on_draw()
            end_drawing()

            self.scene.on_end_frame()

        self.scene.on_destroy()
        close_audio_device()
        close_window()
