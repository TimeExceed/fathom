import fathom.geometry as geo
from ..geometry import Point, origin, centroid

class Canvas:
    def __init__(self, **kws):
        self._preamble = []
        self._shapes = []
        preamble = kws.get('preamble')
        if preamble is not None:
            self._preamble = preamble

    def draw(self):
        insts = []
        for x in self._shapes:
            x.instructions(insts)

        return r'''
\documentclass[UTF8]{{ctexart}}
\usepackage[a0paper]{{geometry}}
\usepackage{{tikz}}
\pagestyle{{empty}}
{}
\begin{{document}}
\begin{{tikzpicture}}
{}
\end{{tikzpicture}}
\end{{document}}
'''.format(
    '\n'.join(self._preamble),
    '\n'.join(insts))

    def new_line(self, **kws):
        kws['arrow_position'] = NONE
        s = _Arrow(**kws)
        self._shapes.append(s)
        return s

    def new_arrow(self, **kws):
        kws['arrow_position'] = TAIL
        s = _Arrow(**kws)
        self._shapes.append(s)
        return s

    def new_dblarrow(self, **kws):
        kws['arrow_position'] = BOTH
        s = _Arrow(**kws)
        self._shapes.append(s)
        return s

    def new_backward_arrow(self, **kws):
        kws['arrow_position'] = HEAD
        s = _Arrow(**kws)
        self._shapes.append(s)
        return s

    def new_circle(self, **kws):
        s = _Circle(**kws)
        self._shapes.append(s)
        return s

def format_float(fp):
    return '{:.2f}cm'.format(fp)

class _Point:
    def __init__(self, pt):
        self._geo = pt

    def __repr__(self):
        return '({},{})'.format(
            format_float(self._geo.x), format_float(self._geo.y))

    def get_skeleton(self):
        return self._geo

def calc_intersect(src, dst):
    if isinstance(src, Point):
        return src
    else:
        src = src.get_skeleton()
        if isinstance(dst, Point):
            return src.intersect_from_center(dst)
        else:
            return src.intersect_from_center(dst.get_skeleton().center())

class _Arrow:
    def __init__(self, **kws):
        src = kws['src']
        dst = kws['dst']
        real_src = calc_intersect(src, dst)
        real_dst = calc_intersect(dst, src)
        self._geo = geo.Arrow(src=real_src, dst=real_dst)
        self._pen_color = _get_pen_color(kws)
        self._brush_color = _get_brush_color(kws)
        self._line_style = _get_line_style(kws)
        self._arrow_position = kws['arrow_position']

    def instructions(self, insts):
        draw_pat = '{cmd} {src} -- {dst};'
        draw = _draw_cmd(self)
        if draw is not None:
            insts.append(draw_pat.format(
                cmd=draw,
                src=_Point(self._geo.src),
                dst=_Point(self._geo.dst),
            ))

    def get_skeleton(self):
        return self._geo

def _get_pen_color(kws):
    pen_color = kws.get('pen_color')
    if pen_color is not None:
        return pen_color
    return BLACK

def _get_brush_color(kws):
    brush_color = kws.get('brush_color')
    if brush_color is not None:
        return brush_color
    return INVISIBLE

def _get_line_style(kws):
    line_style = kws.get('line_style')
    if line_style is not None:
        return line_style
    return SOLID

def _draw_cmd(shape):
    if shape._pen_color is INVISIBLE:
        return None

    opts = []

    if getattr(shape, '_arrow_position', None) is not None and shape._arrow_position is not NONE:
        opts.append('{}'.format(shape._arrow_position))

    if shape._pen_color is not BLACK:
        opts.append('color={}'.format(shape._pen_color))

    if shape._line_style is not SOLID:
        opts.append('{}'.format(shape._line_style))

    if len(opts) == 0:
        return r'\draw'
    else:
        return r'\draw[{opts}]'.format(opts=','.join(opts))

def _fill_cmd(shape):
    if shape._brush_color is INVISIBLE:
        return None

    if shape._brush_color is BLACK:
        return r'\fill'
    else:
        return r'\fill[color={}]'.format(shape._brush_color)

class _Circle:
    def __init__(self, **kws):
        self._geo = geo.Circle(**kws)
        self._pen_color = _get_pen_color(kws)
        self._brush_color = _get_brush_color(kws)
        self._line_style = _get_line_style(kws)

    def get_skeleton(self):
        return self._geo

    def instructions(self, insts):
        center = _Point(self._geo.center())
        radius = self._geo.radius

        draw_pat = '{cmd} {center} circle [radius={radius}];'
        draw = _draw_cmd(self)
        if draw is not None:
            insts.append(draw_pat.format(
                cmd=draw,
                center=center,
                radius=format_float(radius),
            ))

        fill = _fill_cmd(self)
        if fill is not None:
            insts.append(draw_pat.format(
                cmd=fill,
                center=center,
                radius=format_float(radius),
            ))

class _InvisibleColor:
    def __init__(self):
        pass

    def __repr__(self):
        return 'invisible'

INVISIBLE = _InvisibleColor()

class _PredefinedColor:
    def __init__(self, pred):
        self._predefined = pred

    def __repr__(self):
        return self._predefined

    def scale(self, ratio):
        return _ScaledColor(self, ratio)

    def mix(self, other):
        assert type(other) in (_PredefinedColor, _ScaledColor), type(other)
        return _MixedColor([self, other])

BLACK = _PredefinedColor('black')
WHITE = _PredefinedColor('white')
RED = _PredefinedColor('red')
GREEN = _PredefinedColor('green')
BLUE = _PredefinedColor('blue')
CYAN = _PredefinedColor('cyan')
MAGENTA = _PredefinedColor('magenta')
YELLOW = _PredefinedColor('yellow')
GRAY = _PredefinedColor('gray')
DARK_GRAY = _PredefinedColor('darkgray')
LIGHT_GRAY = _PredefinedColor('lightgray')
BROWN = _PredefinedColor('brown')
LIME = _PredefinedColor('lime')
OLIVE = _PredefinedColor('olive')
ORAGNE = _PredefinedColor('orange')
PINK = _PredefinedColor('pink')
PURPLE = _PredefinedColor('purple')
TEAL = _PredefinedColor('teal')
VIOLET = _PredefinedColor('violet')

class _ScaledColor:
    def __init__(self, base, ratio):
        self._base = base
        self._ratio = ratio

    def __repr__(self):
        return '{}!{:.0f}'.format(self._base, self._ratio)

    def mix(self, other):
        assert type(other) in (_PredefinedColor, _ScaledColor), type(other)
        return _MixedColor([self, other])

class _MixedColor:
    def __init__(self, mixes):
        self._mixes = mixes

    def __repr__(self):
        return '!'.join(['{}'.format(x) for x in self._mixes])

    def mix(self, other):
        assert type(other) in (_PredefinedColor, _ScaledColor), type(other)
        mixes = self._mixes[:]
        mixes.append(other)
        return _MixedColor(mixes)

class _LineStyle:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return self._name

DASHED = _LineStyle('dashed')
DOTTED = _LineStyle('dotted')
SOLID = _LineStyle('solid')

class _ArrowPos: pass

class _None(_ArrowPos): pass

class _Tail(_ArrowPos):
    def __repr__(self):
        return '->'

class _Head(_ArrowPos):
    def __repr__(self):
        return '<-'

class _Both(_ArrowPos):
    def __repr__(self):
        return '<->'

NONE = _None()
HEAD = _Head()
TAIL = _Tail()
BOTH = _Both()
