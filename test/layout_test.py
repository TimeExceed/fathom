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

if __name__ == '__main__':
    testa.main()
