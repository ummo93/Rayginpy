from pyray import get_screen_width, get_screen_height
import asyncio

from raylib.enums import ConfigFlags

from app.core.raylib_game import RaylibGame, GameSettings
from app.game.main_scene import MainScene

if __name__ == '__main__':
    settings = GameSettings(
        width=get_screen_width(),
        height=get_screen_height(),
        title="Raygin Python",
        window_flags=ConfigFlags.FLAG_WINDOW_RESIZABLE |
                     ConfigFlags.FLAG_VSYNC_HINT |
                     ConfigFlags.FLAG_FULLSCREEN_MODE |
                     ConfigFlags.FLAG_WINDOW_ALWAYS_RUN
    )
    game = RaylibGame(settings, MainScene())
    game.init()
    asyncio.run(game.start_game_loop())
