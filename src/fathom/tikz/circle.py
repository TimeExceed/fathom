from .utils import *
import fathom.geometry as geo

class Circle:
    def __init__(self, **kws):
        self._geo = geo.Circle(**kws)
        self._pen_color = get_pen_color(kws)
        self._brush_color = get_brush_color(kws)
        self._line_style = get_line_style(kws)

    def get_skeleton(self):
        return self._geo

    def instructions(self, insts):
        center = format_point(self._geo.center())
        radius = format_float(self._geo.radius)

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
