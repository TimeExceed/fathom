__all__ = ['Canvas']

from . import arrow
from . import circle
from . import bullet
from . import text
from . import polygon
from . import little_man


def _add_shape(f):
    def go(*args, **kws):
        # pylint: disable=protected-access
        s = f(*args, **kws)
        args[0]._shapes.append(s)
        return s
    return go


class Canvas:
    def __init__(self, **kws):
        self._preamble = []
        self._shapes = []
        self._leading_insts = []

        preamble = kws.get('preamble')
        if preamble is not None:
            self._preamble.extend(preamble)

        leading_insts = kws.get('leading_instructions')
        if leading_insts is not None:
            self._leading_insts.extend(leading_insts)

    def draw(self):
        insts = []
        for x in self._shapes:
            x.instructions(insts)

        return r'''
\documentclass[UTF8]{{ctexart}}
\usepackage[a0paper]{{geometry}}
\usepackage{{tikz}}
\usetikzlibrary{{arrows.meta,arrows}}
\pagestyle{{empty}}
{}
\begin{{document}}
{}\begin{{tikzpicture}}[>=Stealth]
{}
\end{{tikzpicture}}
\end{{document}}
'''.format('\n'.join(self._preamble),
           '\n'.join(self._leading_insts) + '\n' if self._leading_insts else '',
           '\n'.join(insts))

    # pylint: disable=no-self-use

    @_add_shape
    def new_line(self, *args, **kws):
        kws['arrow_position'] = arrow.NONE
        return arrow.Arrow(*args, **kws)

    @_add_shape
    def new_arrow(self, *args, **kws):
        kws['arrow_position'] = arrow.TAIL
        return arrow.Arrow(*args, **kws)

    @_add_shape
    def new_dblarrow(self, *args, **kws):
        kws['arrow_position'] = arrow.BOTH
        return arrow.Arrow(*args, **kws)

    @_add_shape
    def new_backward_arrow(self, *args, **kws):
        kws['arrow_position'] = arrow.HEAD
        return arrow.Arrow(*args, **kws)

    @_add_shape
    def new_circle(self, *args, **kws):
        return circle.Circle(*args, **kws)

    @_add_shape
    def new_bullet(self, *args, **kws):
        return bullet.Bullet(*args, **kws)

    @_add_shape
    def new_text(self, **kws):
        return text.Text(**kws)

    @_add_shape
    def new_rectangle(self, *args, **kws):
        return polygon.Rectangle(*args, **kws)

    @_add_shape
    def new_triangle(self, *args, **kws):
        return polygon.Triangle(*args, **kws)

    @_add_shape
    def new_polygon(self, *args, **kws):
        return polygon.Polygon(*args, **kws)

    @_add_shape
    def new_little_man(self, *args, **kws):
        return little_man.LittleMan(*args, **kws)

    @_add_shape
    def new_diamond(self, *args, **kws):
        return polygon.Diamond(*args, **kws)
