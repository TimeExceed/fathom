from fathom.geometry import Point
from .utils import format_point
from .opts import *
from . import locations

class Text:
    def __init__(self, **kws):
        self._anchor = kws['anchor']
        assert isinstance(self._anchor, Point)
        self._text = kws['text']
        assert isinstance(self._text, str)
        self._pen_color = get_pen_color(kws)
        self._location = kws.get('location', locations.CENTER)

    def instructions(self, insts):
        opts = []

        if self._pen_color is not colors.BLACK:
            opts.append('color={}'.format(self._pen_color))

        if self._location is not locations.CENTER:
            opts.append('{}'.format(self._location))

        if len(opts) == 0:
            draw_pat = r'\node at {anchor} {{{text}}};'
            insts.append(draw_pat.format(
                anchor=format_point(self._anchor),
                text=self._text,
            ))
        else:
            draw_pat = r'\node[{opts}] at {anchor} {{{text}}};'
            insts.append(draw_pat.format(
                anchor=format_point(self._anchor),
                text=self._text,
                opts=','.join(opts),
            ))

    def get_skeleton(self):
        return self._anchor
