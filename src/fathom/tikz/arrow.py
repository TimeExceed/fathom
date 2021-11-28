import fathom.geometry as geo
from fathom.geometry import Point
from .opts import *
from .shape import Shape

class Arrow(Shape):
    def __init__(self, *args, **kws):
        super().__init__(kws)
        self._arrow_position = kws['arrow_position']
        self._geo = check_geoshape_in_args(geo.Arrow, args)
        if not self._geo:
            # cut arrow by src/dst edges
            src = kws['src']
            dst = kws['dst']
            real_src = _calc_intersect(src, dst)
            real_dst = _calc_intersect(dst, src)  # pylint: disable=arguments-out-of-order
            self._geo = geo.Arrow(src=real_src, dst=real_dst)

    def instructions(self, insts):
        draw_pat = '{cmd} {src} -- {dst};'
        if self._arrow_position is not NONE:
            draw = draw_cmd(self, ['{}'.format(self._arrow_position)])
        else:
            draw = draw_cmd(self)
        if draw is not None:
            insts.append(draw_pat.format(
                cmd=draw,
                src=format_point(self._geo.src),
                dst=format_point(self._geo.dst),
            ))

    def get_skeleton(self):
        return self._geo


def _calc_intersect(src, dst):
    if isinstance(src, Point):
        return src
    elif not isinstance(src, geo.Shape):
        src = src.get_skeleton()
    if isinstance(dst, Point):
        return src.intersect_from_center(dst)
    elif not isinstance(dst, geo.Shape):
        dst = dst.get_skeleton()
    return src.intersect_from_center(dst.center())


class _ArrowPos:  # pylint: disable=too-few-public-methods
    pass


class _None(_ArrowPos):  # pylint: disable=too-few-public-methods
    pass


class _Tail(_ArrowPos):  # pylint: disable=too-few-public-methods
    def __repr__(self):
        return '->'


class _Head(_ArrowPos):  # pylint: disable=too-few-public-methods
    def __repr__(self):
        return '<-'


class _Both(_ArrowPos):  # pylint: disable=too-few-public-methods
    def __repr__(self):
        return '<->'


NONE = _None()
HEAD = _Head()
TAIL = _Tail()
BOTH = _Both()
