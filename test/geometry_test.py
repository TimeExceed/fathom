import testa
from geometry import *
from itertools import *

def point_algebra_tb(case_f):
    ps = [Point(x, y) for x in range(5) for y in range(5)]
    for p0, p1 in permutations(ps, 2):
        res = case_f(p0, p1)
        if res is not None:
            return res

@testa.eq(testbench=point_algebra_tb, oracle=lambda x, _: x)
def point_algebra_trial(p0, p1):
    return p0 + p1 - p1

@testa.is_(expect=Point(1, 1))
def intersect_normal():
    a = Arrow(origin, Point(2, 2))
    b = Arrow(Point(2, 0), Point(0, 2))
    return a.intersect_line(b)

@testa.is_(expect=None)
def intersect_parallel():
    a = Arrow(origin, Point(2, 0))
    b = Arrow(Point(-1, 1), Point(1, 1))
    return a.intersect_line(b)

@testa.is_(expect=origin)
def intersect_from():
    a = Arrow(origin, Point(2, 2))
    b = Arrow(origin, Point(2, 0))
    return a.intersect_line(b)

@testa.is_(expect=Point(2, 2))
def intersect_to():
    a = Arrow(origin, Point(2, 2))
    b = Arrow(Point(0, 2), Point(2, 2))
    return a.intersect_line(b)

@testa.is_(expect=None)
def intersect_outside():
    a = Arrow(origin, Point(2, 0))
    b = Arrow(Point(-1, -1), Point(-1, 1))
    return a.intersect_line(b)

def intersect_exhaustive_tb(case_f):
    ps = [Point(1, 1), Point(1, 2), Point(2, 2), Point(2, 1)]
    arrs = [Arrow(p0, p1) for p0 in ps for p1 in ps if p0 != p1]
    for a0, a1 in permutations(arrs, 2):
        res = case_f(a0, a1)
        if res is not None:
            return res

@testa.verify(
    trial=lambda a0, a1: a0.intersect_line(a1),
    testbench=intersect_exhaustive_tb)
def intersect_exhaustive_verifier(res, a0, a1):
    def norm(arr):
        ps = [arr.from_pt, arr.to_pt]
        ps = sorted(ps, key=lambda p:(p.x, p.y))
        return Arrow(ps[0], ps[1])
    b0 = norm(a0)
    b1 = norm(a1)
    if b0 == b1:
        parallel = True
    elif b0.from_pt.x == b0.to_pt.x and b1.from_pt.x == b1.to_pt.x:
        parallel = True
    elif b0.from_pt.y == b0.to_pt.y and b1.from_pt.y == b1.to_pt.y:
        parallel = True
    else:
        parallel = False
    if parallel != (res is None):
        return 'got {} by applying {} and {}'.format(res, a0, a1)

@testa.is_(expect=Point(1, 1))
def arrow_center():
    return Arrow(origin, Point(2, 2)).center()

if __name__ == '__main__':
    testa.main()
