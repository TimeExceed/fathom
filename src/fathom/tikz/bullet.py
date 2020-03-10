import fathom.geometry as geo
from fathom.geometry import Point
from .utils import *
from .circle import Circle
from . import colors

class Bullet:
    def __init__(self, **kws):
        center = kws['center']
        radius = kws.get('radius', 0.05)
        brush_color = kws.get('brush_color', colors.BLACK)
        pen_color = kws.get('pen_color', colors.INVISIBLE)
        line_style = get_line_style(kws)
        sep = kws.get('sep', 0.01)
        self._inner = Circle(
            center=center,
            radius=radius,
            pen_color=colors.INVISIBLE,
            brush_color=brush_color)
        self._outer = Circle(
            center=center,
            radius=radius + sep,
            pen_color=pen_color,
            line_style=line_style)

    def instructions(self, insts):
        self._inner.instructions(insts)
        self._outer.instructions(insts)

    def get_skeleton(self):
        return self._outer.get_skeleton()
