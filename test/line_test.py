import testa
from fathom import Point, ORIGIN
import fathom.tikz as tikz
import fathom.tikz.colors as colors
import fathom.tikz.line_styles as line_styles

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw (0.00cm,0.00cm) -- (1.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def draw_line():
    canvas = tikz.Canvas()
    canvas.new_line(src=ORIGIN, dst=Point(1, 0))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[->] (0.00cm,0.00cm) -- (1.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def draw_arrow():
    canvas = tikz.Canvas()
    canvas.new_arrow(src=ORIGIN, dst=Point(1, 0))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[<->] (0.00cm,0.00cm) -- (1.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def draw_dblarrow():
    canvas = tikz.Canvas()
    canvas.new_dblarrow(src=ORIGIN, dst=Point(1, 0))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[<-] (0.00cm,0.00cm) -- (1.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def draw_backward_arrow():
    canvas = tikz.Canvas()
    canvas.new_backward_arrow(src=ORIGIN, dst=Point(1, 0))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw (1.00cm,0.00cm) -- (3.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def line_from_shape():
    canvas = tikz.Canvas()
    c0 = canvas.new_circle(center=ORIGIN, radius=1, pen_color=colors.INVISIBLE)
    canvas.new_line(src=c0, dst=Point(3, 0))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw (0.00cm,0.00cm) -- (2.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def line_to_shape():
    canvas = tikz.Canvas()
    c1 = canvas.new_circle(
        center=Point(3, 0),
        radius=1,
        pen_color=colors.INVISIBLE)
    canvas.new_line(src=ORIGIN, dst=c1)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw (1.00cm,0.00cm) -- (2.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def line_between_shapes():
    canvas = tikz.Canvas()
    c0 = canvas.new_circle(
        center=ORIGIN,
        radius=1,
        pen_color=colors.INVISIBLE)
    c1 = canvas.new_circle(
        center=Point(3, 0),
        radius=1,
        pen_color=colors.INVISIBLE)
    canvas.new_line(src=c0, dst=c1)
    return canvas.draw()


if __name__ == '__main__':
    testa.main()
