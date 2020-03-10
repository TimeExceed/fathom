from .utils import *
from .polygon import Polygon
from . import corner_styles
import fathom.geometry as geo


class Rectangle(Polygon):
    def __init__(self, **kws):
        self._geo = geo.Rectangle(**kws)
        self._pen_color = get_pen_color(kws)
        self._brush_color = get_brush_color(kws)
        self._line_style = get_line_style(kws)
        self._corner_style = get_corner_style(kws)

    def get_skeleton(self):
        return self._geo

    def instructions(self, insts):
        more_opts = []

        if self._corner_style is not corner_styles.SHARP:
            rc = '{}'.format(self._corner_style)
            more_opts.append(rc)

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

