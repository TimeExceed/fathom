__all__ = ['Rectangle', 'Triangle', 'Polygon']

from typing import Union, List
import fathom.geometry as geo
from .utils import *
from .opts import *
from .shape import Shape
from .. import corner_styles

class _PolygonBase(Shape):
    def __init__(self, expect_cls, args, kws):
        super().__init__(kws)
        self._geo = default_construct_shape(expect_cls, args, kws)

    def instructions(self, insts):
        more_opts = []

        draw_corner(more_opts, self._corner_style)

        vertices = [format_point(x) for x in self._geo.vertices()]
        vertices = '--'.join(vertices)
        draw_pat = '{cmd} {vertices}--cycle;'

        fill = fill_cmd(self, additional_opts=more_opts)
        if fill is not None:
            insts.append(draw_pat.format(
                cmd=fill,
                vertices=vertices,
            ))

        draw = draw_cmd(self, additional_opts=more_opts)
        if draw is not None:
            insts.append(draw_pat.format(
                cmd=draw,
                vertices=vertices,
            ))

def draw_corner(opts: List[str], corner: Union[corner_styles._Sharp, corner_styles.Rounded]):
    if corner is not corner_styles.SHARP:
        opt = 'rounded corners={}'.format(format_length(corner.radius))
        opts.append(opt)

class Polygon(_PolygonBase):
    def __init__(self, *args, **kws):
        super().__init__(geo.Polygon, args, kws)


class Rectangle(_PolygonBase):
    def __init__(self, *args, **kws):
        super().__init__(geo.Rectangle, args, kws)


class Triangle(_PolygonBase):
    def __init__(self, *args, **kws):
        super().__init__(geo.Triangle, args, kws)

class Diamond(_PolygonBase):
    def __init__(self, *args, **kws):
        super().__init__(geo.Diamond, args, kws)
