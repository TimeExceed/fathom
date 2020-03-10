import testa
from fathom import Point, origin
import fathom.tikz as tikz
import fathom.tikz.colors as colors
import fathom.tikz.line_styles as line_styles
import fathom.tikz.corner_styles as corner_styles

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw (0.50cm,2.00cm)--(1.50cm,2.00cm)--(1.50cm,0.00cm)--(0.50cm,0.00cm)--cycle;
\end{tikzpicture}
\end{document}
''')
def draw_rectangle():
    canvas = tikz.Canvas()
    canvas.new_rectangle(center=Point(1, 1), width=1, height=2)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[color=red] (0.50cm,2.00cm)--(1.50cm,2.00cm)--(1.50cm,0.00cm)--(0.50cm,0.00cm)--cycle;
\end{tikzpicture}
\end{document}
''')
def rectangle_pen_color():
    canvas = tikz.Canvas()
    canvas.new_rectangle(
        center=Point(1, 1),
        width=1,
        height=2,
        pen_color=colors.RED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\fill[color=red] (0.50cm,2.00cm)--(1.50cm,2.00cm)--(1.50cm,0.00cm)--(0.50cm,0.00cm)--cycle;
\end{tikzpicture}
\end{document}
''')
def rectangle_brush_color():
    canvas = tikz.Canvas()
    canvas.new_rectangle(
        center=Point(1, 1),
        width=1,
        height=2,
        pen_color=colors.INVISIBLE,
        brush_color=colors.RED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[dashed] (0.50cm,2.00cm)--(1.50cm,2.00cm)--(1.50cm,0.00cm)--(0.50cm,0.00cm)--cycle;
\end{tikzpicture}
\end{document}
''')
def rectangle_line_style():
    canvas = tikz.Canvas()
    canvas.new_rectangle(
        center=Point(1, 1),
        width=1,
        height=2,
        line_style=line_styles.DASHED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\fill[rounded corners=0.15cm,color=red] (0.50cm,2.00cm)--(1.50cm,2.00cm)--(1.50cm,0.00cm)--(0.50cm,0.00cm)--cycle;
\draw[rounded corners=0.15cm] (0.50cm,2.00cm)--(1.50cm,2.00cm)--(1.50cm,0.00cm)--(0.50cm,0.00cm)--cycle;
\end{tikzpicture}
\end{document}
''')
def rectangle_rounded_corners():
    canvas = tikz.Canvas()
    canvas.new_rectangle(
        center=Point(1, 1),
        width=1,
        height=2,
        pen_color=colors.BLACK,
        brush_color=colors.RED,
        corner_style=corner_styles.DEFAULT_ROUNDED)
    return canvas.draw()


if __name__ == '__main__':
    testa.main()
