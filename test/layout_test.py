import testa
from geometry import *
from layout import *
from itertools import *

@testa.is_(
    expect=[
        [origin, Point(1, 0), Point(2, 0)],
        [Point(0, -2), Point(1, -2), Point(2, -2)],
    ]
)
def matrix_ctor():
    return matrix(top_left=origin, h_sep=1, v_sep=2, n_rows=2, n_cols=3)


@testa.is_(
    expect={
        'root': origin,
        'child': Point(0, -1)
    }
)
def tree_verticle_line():
    s = ['root', ['child']]
    return tree(s, root=origin, h_sep=1, v_sep=1)

@testa.is_(
    expect={
        'root': origin,
        'left': Point(-1, -1),
        'right': Point(1, -1),
    }
)
def tree_triangle():
    s = ['root', ['left'], ['right']]
    return tree(s, root=origin, h_sep=2, v_sep=1)

@testa.is_(
    expect={
        'root': origin,
        'left': Point(-2, -1),
        'middle': Point(0, -1),
        'right': Point(2, -1),
        'm_left': Point(-1, -2),
        'm_right': Point(1, -2),
    }
)
def tree_hierarchical():
    s = ['root', ['left'], ['middle', ['m_left'], ['m_right']], ['right']]
    return tree(s, root=origin, h_sep=2, v_sep=1)

@testa.is_(
    expect={
        'root': origin,
        'left': Point(-3, -1),
        'middle': Point(0, -1),
        'right': Point(3, -1),
        'l_left': Point(-5, -2),
        'l_middle': Point(-3, -2),
        'l_right': Point(-1, -2),
        'r_left': Point(1, -2),
        'r_middle': Point(3, -2),
        'r_right': Point(5, -2),
    }
)
def tree_bridge():
    s = [
        'root',
        ['left', ['l_left'], ['l_middle'], ['l_right']],
        ['middle'],
        ['right', ['r_left'], ['r_middle'], ['r_right']],
    ]
    return tree(s, root=origin, h_sep=2, v_sep=1)

@testa.is_(
    expect={
        'root': origin,
        'left': Point(-1.5, -1),
        'right': Point(1.5, -1),
        'r0': Point(-1.5, -2),
        'r1': Point(0.5, -2),
        'r2': Point(2.5, -2),
        'r3': Point(4.5, -2),
    }
)
def tree_inbalanced():
    s = [
        'root',
        ['left'],
        ['right', ['r0'], ['r1'], ['r2'], ['r3']],
    ]
    return tree(s, root=origin, h_sep=2, v_sep=1)

@testa.is_(
    expect={
        'root': origin,
        'left': Point(-1, -1),
        'right': Point(1, -1),
        'r0': Point(1, -2),
    }
)
def tree_slope():
    s = [
        'root',
        ['left'],
        ['right', ['r0']],
    ]
    return tree(s, root=origin, h_sep=2, v_sep=1)

if __name__ == '__main__':
    testa.main()
