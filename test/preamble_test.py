import testa
import fathom.tikz as tikz


@testa.is_(expect=r'''
\documentclass[UTF8]{ctexart}
\usepackage[a0paper]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows}
\pagestyle{empty}
xxx
\begin{document}
yyy
\begin{tikzpicture}[>=Stealth]

\end{tikzpicture}
\end{document}
''')
def preamble():
    canvas = tikz.Canvas(preamble=['xxx'], leading_instructions=['yyy'])
    return canvas.draw()


if __name__ == '__main__':
    testa.main()
