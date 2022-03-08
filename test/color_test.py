import testa
from fathom import Point, ORIGIN
import fathom.tikz as tikz
import fathom.colors as colors

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
\fill[color=black!50] (1.00cm,1.00cm) circle [radius=1.00cm];
\draw[color=red!50] (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def scaled_color():
    canvas = tikz.Canvas()
    canvas.new_circle(center=Point(1, 1), radius=1,
                      pen_color=colors.RED.scale(0.5),
                      brush_color=colors.BLACK.scale(0.5))
    return canvas.draw()


@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
\fill[color=black!white] (1.00cm,1.00cm) circle [radius=1.00cm];
\draw[color=red!green] (1.00cm,1.00cm) circle [radius=1.00cm];
\end{tikzpicture}
\end{document}
''')
def mixed_color():
    canvas = tikz.Canvas()
    canvas.new_circle(center=Point(1, 1), radius=1,
                      pen_color=colors.RED.mix(colors.GREEN),
                      brush_color=colors.BLACK.mix(colors.WHITE))
    return canvas.draw()

if __name__ == '__main__':
    testa.main()
