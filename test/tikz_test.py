import testa
from fathom import Point, origin
import fathom.driver.tikz as tikz

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
    c0 = canvas.new_circle(center=origin, radius=1, pen_color=tikz.INVISIBLE)
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
        pen_color=tikz.INVISIBLE)
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
        pen_color=tikz.INVISIBLE)
    c1 = canvas.new_circle(
        center=Point(3, 0),
        radius=1,
        pen_color=tikz.INVISIBLE)
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
    canvas.new_circle(center=Point(1, 1), radius=1, pen_color=tikz.RED)
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
    canvas.new_circle(center=Point(1, 1), radius=1, pen_color=tikz.INVISIBLE)
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
    canvas.new_circle(center=Point(1, 1), radius=1, pen_color=tikz.RED.scale(50))
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
        pen_color=tikz.RED.scale(50).mix(tikz.GREEN))
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
        pen_color=tikz.INVISIBLE,
        brush_color=tikz.RED)
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
        line_style=tikz.DASHED)
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
        line_style=tikz.DOTTED)
    return canvas.draw()

if __name__ == '__main__':
    testa.main()
