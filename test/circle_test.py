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
\draw (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def draw_circle():
    canvas = tikz.Canvas()
    canvas.new_circle(center=Point(1, 1), radius=1)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[color=red] (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def circle_pen_color():
    canvas = tikz.Canvas()
    canvas.new_circle(center=Point(1, 1), radius=1, pen_color=colors.RED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}

\end{tikzpicture}
\end{document}
''')
def invisible_circle():
    canvas = tikz.Canvas()
    canvas.new_circle(
        center=Point(1, 1),
        radius=1,
        pen_color=colors.INVISIBLE)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[color=red!50] (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def circle_scaled_color():
    canvas = tikz.Canvas()
    canvas.new_circle(center=Point(1, 1), radius=1,
                      pen_color=colors.RED.scale(50))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[color=red!50!green] (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def circle_mixed_color():
    canvas = tikz.Canvas()
    canvas.new_circle(
        center=Point(1, 1),
        radius=1,
        pen_color=colors.RED.scale(50).mix(colors.GREEN))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\fill[color=red] (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def fill_circle():
    canvas = tikz.Canvas()
    canvas.new_circle(
        center=Point(1, 1),
        radius=1,
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
\draw[dashed] (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def draw_dashed_circle():
    canvas = tikz.Canvas()
    canvas.new_circle(
        center=Point(1, 1),
        radius=1,
        line_style=line_styles.DASHED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\draw[dotted] (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def draw_dotted_circle():
    canvas = tikz.Canvas()
    canvas.new_circle(
        center=Point(1, 1),
        radius=1,
        line_style=line_styles.DOTTED)
    return canvas.draw()


if __name__ == '__main__':
    testa.main()
