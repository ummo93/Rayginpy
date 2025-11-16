from pyray import Color, rl_begin, rl_vertex2f, rl_color4ub, rl_end, Vector2
from raylib.defines import RL_LINES

def draw_lines_batch(segments: list[tuple[float, float]], color: Color, fade: bool = False, fade_strength: int = 1):
    if len(segments) == 0: return
    rl_begin(RL_LINES)
    a_max = color.a
    a_cur = 0 if fade else a_max
    for (i, (x, y)) in enumerate(segments):
        if fade:
            a_cur += fade_strength if a_cur < a_max else 0
            if a_cur > a_max: a_cur = a_max
        rl_color4ub(color.r, color.g, color.b, a_cur)
        rl_vertex2f(x, y)
        if i != 0:
            rl_vertex2f(segments[i-1][0], segments[i-1][1])
    rl_end()



def midpoint(a: Vector2, b: Vector2) -> Vector2:
    return Vector2((a.x + b.x) / 2, (a.y + b.y) / 2)