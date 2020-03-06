from geometry import *

def matrix(**kws):
    h_sep = float(kws['h_sep'])
    v_sep = float(kws['v_sep'])
    n_rows = kws['n_rows']
    assert type(n_rows) == int, type(n_rows)
    n_cols = kws['n_cols']
    assert type(n_cols) == int, type(n_cols)
    top_left = kws['top_left']
    assert type(top_left) == Point, type(top_left)
    return [
        [top_left + Point(h_sep*x, -v_sep*y) for x in range(n_cols)]\
            for y in range(n_rows)
    ]
