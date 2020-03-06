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
        s = _Line(kws)
        self._shapes.append(s)
        return s

class _Point:
    def __init__(self, pt):
        self._geo = pt

    def __repr__(self):
        return '({:.2f}cm,{:.2f}cm)'.format(self._geo.x, self._geo.y)

class _Line:
    def __init__(self, kws):
        self._geo = geo.Arrow(**kws)

    def instructions(self, insts):
        vs = self._geo.vertices()
        vs = tuple(_Point(x) for x in vs)
        insts.append(r'\draw {} -- {};'.format(*vs))
