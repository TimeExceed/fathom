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
\fill (1.00cm,1.00cm) circle [radius=0.05cm];
\end{tikzpicture}
\end{document}
''')
def bullet():
    canvas = tikz.Canvas()
    canvas.new_bullet(center=Point(1, 1))
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
\fill[color=red] (1.00cm,1.00cm) circle [radius=0.05cm];
\end{tikzpicture}
\end{document}
''')
def colored_bullet():
    canvas = tikz.Canvas()
    canvas.new_bullet(center=Point(1, 1), brush_color=colors.RED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
\fill (1.00cm,1.00cm) circle [radius=0.05cm];
\draw[color=red] (1.00cm,1.00cm) circle [radius=0.06cm];
\end{tikzpicture}
\end{document}
''')
def rounded_bullet():
    canvas = tikz.Canvas()
    canvas.new_bullet(
        center=Point(1, 1),
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
\fill (1.00cm,1.00cm) circle [radius=0.05cm];
\draw[color=red] (1.00cm,1.00cm) circle [radius=0.10cm];
\end{tikzpicture}
\end{document}
''')
def bullet_sep():
    canvas = tikz.Canvas()
    canvas.new_bullet(
        center=Point(1, 1),
        pen_color=colors.RED,
        sep=0.05)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
\fill (1.00cm,1.00cm) circle [radius=0.05cm];
\draw[color=red,dashed] (1.00cm,1.00cm) circle [radius=0.06cm];
\end{tikzpicture}
\end{document}
''')
def bullet_outer_line_style():
    canvas = tikz.Canvas()
    canvas.new_bullet(
        center=Point(1, 1),
        pen_color=colors.RED,
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
\fill (0.00cm,0.00cm) circle [radius=0.05cm];
\draw (0.06cm,0.00cm) -- (1.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def intersect_bullet():
    canvas = tikz.Canvas()
    s = canvas.new_bullet(center=ORIGIN)
    canvas.new_line(src=s, dst=Point(1, 0))
    return canvas.draw()


if __name__ == '__main__':
    testa.main()
