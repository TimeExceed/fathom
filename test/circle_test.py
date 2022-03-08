import testa
from fathom import Point, ORIGIN
import fathom.tikz as tikz
import fathom.colors as colors
import fathom.line_styles as line_styles

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]

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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
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
