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

if __name__ == '__main__':
    testa.main()
