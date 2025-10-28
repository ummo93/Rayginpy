from asyncio import sleep
import asyncio
from app.core.scene import *
from app.game.MainScene import MainScene



async def main(width: int, height: int, current_scene: Scene):
    init_window(width, height, current_scene.name)
    current_scene.ready()
    while not window_should_close():
        current_scene.render()
        await sleep(0)
        if current_scene.restart:
            current_scene = MainScene()
            current_scene.ready()
    close_window()


if __name__ == '__main__':
    asyncio.run(main(800, 600, MainScene()))
