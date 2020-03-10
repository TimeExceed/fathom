import testa
from fathom import Point, origin
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
    canvas.new_line(src=origin, dst=Point(1, 0))
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
    canvas.new_arrow(src=origin, dst=Point(1, 0))
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
    canvas.new_dblarrow(src=origin, dst=Point(1, 0))
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
    canvas.new_backward_arrow(src=origin, dst=Point(1, 0))
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
    c0 = canvas.new_circle(center=origin, radius=1, pen_color=colors.INVISIBLE)
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
    canvas.new_line(src=origin, dst=c1)
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
        center=origin,
        radius=1,
        pen_color=colors.INVISIBLE)
    c1 = canvas.new_circle(
        center=Point(3, 0),
        radius=1,
        pen_color=colors.INVISIBLE)
    canvas.new_line(src=c0, dst=c1)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}
xxx
yyy
\begin{document}
\begin{tikzpicture}

\end{tikzpicture}
\end{document}
''')
def preamble():
    canvas = tikz.Canvas(preamble=['xxx', 'yyy'])
    return canvas.draw()

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
    canvas.new_circle(center=Point(1, 1), radius=1, pen_color=colors.RED.scale(50))
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

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
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
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
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
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
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
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
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
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
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
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}
\fill (0.00cm,0.00cm) circle [radius=0.05cm];
\draw (0.06cm,0.00cm) -- (1.00cm,0.00cm);
\end{tikzpicture}
\end{document}
''')
def intersect_bullet():
    canvas = tikz.Canvas()
    s = canvas.new_bullet(center=origin)
    canvas.new_line(src=s, dst=Point(1, 0))
    return canvas.draw()

if __name__ == '__main__':
    testa.main()
