from raylib import FLAG_WINDOW_ALWAYS_RUN, FLAG_WINDOW_RESIZABLE, FLAG_VSYNC_HINT

from app.core.raylib_game import RaylibGame
from app.game.main_scene import MainScene


class Settings:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.title = "Raygin Python".encode()
        self.target_fps = 60
        self.window_flags = FLAG_WINDOW_ALWAYS_RUN | FLAG_WINDOW_RESIZABLE | FLAG_VSYNC_HINT


if __name__ == '__main__':
    settings = Settings()
    game = RaylibGame(settings, MainScene())
    game.init()
    game.start_game_loop()
