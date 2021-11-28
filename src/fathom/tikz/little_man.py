from .polygon import Rectangle
from .circle import Circle
from .arrow import Arrow, NONE
from .opts import *
from .shape import Shape
from .. import geometry as geo
from .. import colors

class LittleMan(Shape):
    def __init__(self, *args, **kws):
        self._bbox = default_construct_shape(geo.Rectangle, args, kws)
        brush_color = kws.get('brush_color', colors.INVISIBLE)
        pen_color = kws.get('pen_color', colors.BLACK)
        line_style = get_line_style(kws)
        sep = kws.get('sep', 0.01)
        vs = self._bbox.vertices()
        ll = vs[3] + Point(sep, sep)
        ur = vs[1] - Point(sep, sep)
        width = ur.x - ll.x
        height = ur.y - ll.y
        
        head_radius = min(width, height * 0.4) / 2
        head_center = Point(ll.x + width / 2, ur.y - head_radius)
        head = Circle(
            center = head_center,
            radius = head_radius,
            line_style = line_style,
            pen_color = pen_color,
            brush_color = brush_color,
        )
        arm = Arrow(
            src = Point(ll.x, ll.y + height / 2),
            dst = Point(ur.x, ll.y + height / 2),
            line_style = line_style,
            pen_color = pen_color,
            arrow_position = NONE,
        )
        body = Arrow(
            src = Point((ll.x + ur.x) / 2, ur.y - head_radius * 2),
            dst = Point((ll.x + ur.x) / 2, ll.y + height / 4),
            line_style = line_style,
            pen_color = pen_color,
            arrow_position = NONE,
        )
        left_leg = Arrow(
            src = Point((ll.x + ur.x) / 2, ll.y + height / 4),
            dst = Point(ll.x + width / 4, ll.y),
            line_style = line_style,
            pen_color = pen_color,
            arrow_position = NONE,
        )
        right_leg = Arrow(
            src = Point((ll.x + ur.x) / 2, ll.y + height / 4),
            dst = Point(ur.x - width / 4, ll.y),
            line_style = line_style,
            pen_color = pen_color,
            arrow_position = NONE,
        )
        self._inner = [
            head,
            body,
            arm,
            left_leg,
            right_leg,
        ]

    def instructions(self, insts):
        for x in self._inner:
            x.instructions(insts)

    def get_skeleton(self):
        return self._bbox
