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

def tree(skeleton, **kws):
    root_pt = kws['root']
    assert type(root_pt) == Point, type(root_pt)
    h_sep = float(kws['h_sep'])
    v_sep = float(kws['v_sep'])
    nodes = {}

    def _shift(skeleton, diff):
        root = skeleton[0]
        p = nodes[root]
        nodes[root] += diff
        for x in skeleton[1:]:
            _shift(x, diff)

    def _init_nodes(skeleton, level):
        assert type(skeleton) == list, skeleton
        rt = skeleton[0]
        assert rt not in nodes, 'duplicated key: {}'.format(rt)
        nodes[rt] = Point(0, - v_sep * level)
        for x in skeleton[1:]:
            _init_nodes(x, level + 1)

    _init_nodes(skeleton, 0)

    levelled_max_x = {}

    def _init_levelled_max_x(skeleton, level):
        if level not in levelled_max_x:
            levelled_max_x[level] = -h_sep
        for x in skeleton[1:]:
            _init_levelled_max_x(x, level + 1)

    _init_levelled_max_x(skeleton, 0)

    def _fix_levelled_max_x(skeleton, level):
        root = nodes[skeleton[0]]
        levelled_max_x[level] = max(root.x, levelled_max_x[level])
        for x in skeleton[1:]:
            _fix_levelled_max_x(x, level + 1)

    def _arrange(skeleton, level):
        root = nodes[skeleton[0]]
        if len(skeleton) == 1:
            root.x = max(root.x, levelled_max_x[level] + h_sep)
        else:
            xs = [_arrange(x, level + 1) for x in skeleton[1:]]
            min_x = min(xs)
            max_x = max(xs)
            root.x = (min_x + max_x) / 2
            if levelled_max_x[level] + h_sep > root.x:
                d = Point(levelled_max_x[level] + h_sep - root.x, 0)
                _shift(skeleton, d)

            if len(skeleton) > 3:
                inc = range(1, len(skeleton))
                dec = range(len(skeleton) - 1, 0, -1)
                ss = [(start, stop)
                      for start, stop in zip(inc, dec) if start < stop]
                for start, stop in ss:
                    n = stop - start
                    start_nd = nodes[skeleton[start][0]]
                    stop_nd = nodes[skeleton[stop][0]]
                    avg_sep = (stop_nd.x - start_nd.x) / n
                    for i in range(start + 1, stop):
                        x = start_nd.x + avg_sep * (i - start)
                        i_nd = nodes[skeleton[i][0]]
                        if x > i_nd.x:
                            d = Point(x - i_nd.x, 0)
                            _shift(skeleton[i], d)

        _fix_levelled_max_x(skeleton, level)
        return root.x

    _arrange(skeleton, 0)

    diff = root_pt - nodes[skeleton[0]]
    _shift(skeleton, diff)
    return nodes
