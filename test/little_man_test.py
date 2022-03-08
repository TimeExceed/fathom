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
\draw (0.00cm,1.19cm) circle [radius=0.80cm];
\draw (0.00cm,0.40cm) -- (0.00cm,-0.99cm);
\draw (-1.49cm,0.00cm) -- (1.49cm,0.00cm);
\draw (0.00cm,-0.99cm) -- (-0.74cm,-1.99cm);
\draw (0.00cm,-0.99cm) -- (0.74cm,-1.99cm);
\end{tikzpicture}
\end{document}
''')
def draw_little_man():
    canvas = tikz.Canvas()
    canvas.new_little_man(center=ORIGIN, width=3, height=4)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
\draw[color=red] (0.00cm,1.19cm) circle [radius=0.80cm];
\draw[color=red] (0.00cm,0.40cm) -- (0.00cm,-0.99cm);
\draw[color=red] (-1.49cm,0.00cm) -- (1.49cm,0.00cm);
\draw[color=red] (0.00cm,-0.99cm) -- (-0.74cm,-1.99cm);
\draw[color=red] (0.00cm,-0.99cm) -- (0.74cm,-1.99cm);
\end{tikzpicture}
\end{document}
''')
def draw_red_little_man():
    canvas = tikz.Canvas()
    canvas.new_little_man(center=ORIGIN, width=3, height=4, pen_color=colors.RED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
\fill[color=red] (0.00cm,1.19cm) circle [radius=0.80cm];
\draw (0.00cm,1.19cm) circle [radius=0.80cm];
\draw (0.00cm,0.40cm) -- (0.00cm,-0.99cm);
\draw (-1.49cm,0.00cm) -- (1.49cm,0.00cm);
\draw (0.00cm,-0.99cm) -- (-0.74cm,-1.99cm);
\draw (0.00cm,-0.99cm) -- (0.74cm,-1.99cm);
\end{tikzpicture}
\end{document}
''')
def draw_little_man_with_red_head():
    canvas = tikz.Canvas()
    canvas.new_little_man(center=ORIGIN, width=3, height=4, brush_color=colors.RED)
    return canvas.draw()

@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}

\begin{document}
\begin{tikzpicture}[>=Stealth]
\draw[dotted] (0.00cm,1.19cm) circle [radius=0.80cm];
\draw[dotted] (0.00cm,0.40cm) -- (0.00cm,-0.99cm);
\draw[dotted] (-1.49cm,0.00cm) -- (1.49cm,0.00cm);
\draw[dotted] (0.00cm,-0.99cm) -- (-0.74cm,-1.99cm);
\draw[dotted] (0.00cm,-0.99cm) -- (0.74cm,-1.99cm);
\end{tikzpicture}
\end{document}
''')
def draw_dotted_little_man():
    canvas = tikz.Canvas()
    canvas.new_little_man(center=ORIGIN, width=3, height=4, line_style=line_styles.DOTTED)
    return canvas.draw()

if __name__ == '__main__':
    testa.main()
