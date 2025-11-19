from dataclasses import dataclass

from pyray import get_screen_width, get_screen_height
import asyncio

from raylib.enums import ConfigFlags

from app.core.raylib_game import RaylibGame, GameSettings
from app.game.main_scene import MainScene

@dataclass
class Settings(GameSettings):
    width: int = get_screen_width()
    height: int = get_screen_height()
    title: str = "Raygin Python"
    window_flags: ConfigFlags = ConfigFlags.FLAG_WINDOW_RESIZABLE | ConfigFlags.FLAG_VSYNC_HINT | \
                                ConfigFlags.FLAG_FULLSCREEN_MODE | ConfigFlags.FLAG_WINDOW_ALWAYS_RUN | \
                                ConfigFlags.FLAG_BORDERLESS_WINDOWED_MODE


if __name__ == '__main__':
    settings = Settings()
    game = RaylibGame(settings, MainScene())
    game.init()
    asyncio.run(game.start_game_loop())
