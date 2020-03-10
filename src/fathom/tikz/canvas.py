__all__ = ['Canvas']

from . import arrow
from . import circle
from . import bullet

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
        kws['arrow_position'] = arrow.NONE
        s = arrow.Arrow(**kws)
        self._shapes.append(s)
        return s

    def new_arrow(self, **kws):
        kws['arrow_position'] = arrow.TAIL
        s = arrow.Arrow(**kws)
        self._shapes.append(s)
        return s

    def new_dblarrow(self, **kws):
        kws['arrow_position'] = arrow.BOTH
        s = arrow.Arrow(**kws)
        self._shapes.append(s)
        return s

    def new_backward_arrow(self, **kws):
        kws['arrow_position'] = arrow.HEAD
        s = arrow.Arrow(**kws)
        self._shapes.append(s)
        return s

    def new_circle(self, **kws):
        s = circle.Circle(**kws)
        self._shapes.append(s)
        return s

    def new_bullet(self, **kws):
        s = bullet.Bullet(**kws)
        self._shapes.append(s)
        return s
