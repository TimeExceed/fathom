import testa
from fathom import Point, ORIGIN
import fathom.tikz as tikz
import fathom.colors as colors
import fathom.line_styles as line_styles
import fathom.locations as locations

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
