import fathom.geometry as geo
from .utils import *
from .opts import *
from .shape import Shape

class Circle(Shape):
    def __init__(self, *args, **kws):
        super().__init__(kws)
        self._geo = default_construct_shape(geo.Circle, args, kws)

    def get_skeleton(self):
        return self._geo

    def instructions(self, insts):
        center = format_point(self._geo.center())
        radius = format_length(self._geo.radius)

        draw_pat = '{cmd} {center} circle [radius={radius}];'

        fill = fill_cmd(self)
        if fill is not None:
            insts.append(draw_pat.format(
                cmd=fill,
                center=center,
                radius=radius,
            ))

        draw = draw_cmd(self)
        if draw is not None:
            insts.append(draw_pat.format(
                cmd=draw,
                center=center,
                radius=radius,
            ))
