import testa
from fathom import Point, origin
import fathom.tikz as tikz
import fathom.tikz.colors as colors
import fathom.tikz.line_styles as line_styles
import fathom.tikz.locations as locations

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[color=red] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def colored_text():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        pen_color=colors.RED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[above] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text_at_north():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        location=locations.NORTH)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[below] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text_at_south():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        location=locations.SOUTH)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[left] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text_at_west():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        location=locations.WEST)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[right] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text_at_east():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        location=locations.EAST)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[above right] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text_at_northeast():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        location=locations.NORTHEAST)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[below right] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text_at_southeast():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        location=locations.SOUTHEAST)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[below left] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text_at_southwest():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        location=locations.SOUTHWEST)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\node[above left] at (1.00cm,1.00cm) {Hello};
\end{tikzpicture}
\end{document}
''')
def text_at_northwest():
    canvas = tikz.Canvas()
    canvas.new_text(
        text='Hello',
        anchor=Point(1, 1),
        location=locations.NORTHWEST)
    return canvas.draw()

if __name__ == '__main__':
    testa.main()
