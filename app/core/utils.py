from pyray import Color, rl_begin, rl_vertex2f, rl_color4ub, rl_end
from raylib.defines import RL_LINES


def draw_lines_batch(segments: list[tuple[float, float]], color: Color, fade: bool = False, fade_str: int = 1):
    if len(segments) == 0: return
    rl_begin(RL_LINES)
    a_max = color.a
    a_cur = 0 if fade else a_max
    for (x, y) in segments:
        if fade:
            a_cur += fade_str if a_cur < a_max else 0
            if a_cur > a_max: a_cur = a_max
        rl_color4ub(color.r, color.g, color.b, a_cur)
        rl_vertex2f(x, y)
    rl_end()