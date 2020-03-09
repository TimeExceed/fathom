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
        s = _Line(**kws)
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

class _Line:
    def __init__(self, **kws):
        self._geo = geo.Arrow(**kws)

    def instructions(self, insts):
        vs = self._geo.vertices()
        vs = tuple(_Point(x) for x in vs)
        insts.append(r'\draw {} -- {};'.format(*vs))

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

class _Circle:
    def __init__(self, **kws):
        self._geo = geo.Circle(**kws)
        self._pen_color = _get_pen_color(kws)
        self._brush_color = _get_brush_color(kws)

    def instructions(self, insts):
        center = _Point(self._geo.center())
        radius = self._geo.radius

        if self._pen_color is not INVISIBLE:
            opts = []
            opts.append('color={}'.format(self._pen_color))

            if len(opts) == 0:
                draw_pat = r'\draw {center} circle [radius={radius}];'
            else:
                draw_pat = r'\draw[{opts}] {center} circle [radius={radius}];'
            insts.append(draw_pat.format(
                opts=(','.join(opts)),
                center=center,
                radius=format_float(radius),
            ))

        if self._brush_color is not INVISIBLE:
            opts = []
            opts.append('color={}'.format(self._brush_color))

            if len(opts) == 0:
                fill_pat = r'\fill {center} circle [radius={radius}];'
            else:
                fill_pat = r'\fill[{opts}] {center} circle [radius={radius}];'
            insts.append(fill_pat.format(
                opts=(','.join(opts)),
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
