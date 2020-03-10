import testa
import fathom.tikz as tikz


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
