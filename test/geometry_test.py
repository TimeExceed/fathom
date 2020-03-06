import testa
from math import sqrt, fabs
from fathom.geometry import *
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

@testa.is_(expect=None)
def intersect_outside():
    a = Arrow(src=origin, dst=Point(2, 0))
    b = Arrow(src=Point(-1, -1), dst=Point(-1, 1))
    return a.intersect_line(b)

def intersect_exhaustive_tb(case_f):
    ps = [Point(1, 1), Point(1, 2), Point(2, 2), Point(2, 1)]
    arrs = [Arrow(src=p0, dst=p1) for p0 in ps for p1 in ps if p0 != p1]
    for a0, a1 in permutations(arrs, 2):
        res = case_f(a0, a1)
        if res is not None:
            return res

@testa.verify(
    trial=lambda a0, a1: a0.intersect_line(a1),
    testbench=intersect_exhaustive_tb)
def intersect_exhaustive_verifier(res, a0, a1):
    def norm(arr):
        ps = [arr.src, arr.dst]
        ps = sorted(ps, key=lambda p:(p.x, p.y))
        return Arrow(src=ps[0], dst=ps[1])
    b0 = norm(a0)
    b1 = norm(a1)
    if b0 == b1:
        parallel = True
    elif b0.src.x == b0.dst.x and b1.src.x == b1.dst.x:
        parallel = True
    elif b0.src.y == b0.dst.y and b1.src.y == b1.dst.y:
        parallel = True
    else:
        parallel = False
    if parallel != (res is None):
        return 'got {} by applying {} and {}'.format(res, a0, a1)

@testa.is_(expect=Point(1, 1))
def arrow_center():
    a = Arrow(src=origin, dst=Point(2, 2))
    return a.center()

@testa.is_(expect=origin)
def circle_center():
    c = Circle(center=origin, radius=1)
    return c.center()

@testa.is_(expect=Point(2, 3))
def circle_intersect_north():
    c = Circle(center=Point(2, 2), radius=1)
    return c.intersect_from_center(Point(2, 4))

@testa.is_(expect=Point(3, 2))
def circle_intersect_east():
    c = Circle(center=Point(2, 2), radius=1)
    return c.intersect_from_center(Point(4, 2))

@testa.is_(expect=Point(2, 1))
def circle_intersect_south():
    c = Circle(center=Point(2, 2), radius=1)
    return c.intersect_from_center(Point(2, 0))

@testa.is_(expect=Point(1, 2))
def circle_intersect_west():
    c = Circle(center=Point(2, 2), radius=1)
    return c.intersect_from_center(Point(0, 2))

@testa.is_(expect=Point(2, 2) + Point(1/sqrt(2), 1/sqrt(2)))
def circle_intersect_northeast():
    c = Circle(center=Point(2, 2), radius=1)
    return c.intersect_from_center(Point(4, 4))

@testa.is_(expect=Point(2, 2) + Point(1/sqrt(2), -1/sqrt(2)))
def circle_intersect_southeast():
    c = Circle(center=Point(2, 2), radius=1)
    return c.intersect_from_center(Point(4, 0))

@testa.is_(expect=Point(2, 2) + Point(-1/sqrt(2), 1/sqrt(2)))
def circle_intersect_northwest():
    c = Circle(center=Point(2, 2), radius=1)
    return c.intersect_from_center(Point(0, 4))

@testa.is_(expect=Point(2, 2) + Point(-1/sqrt(2), -1/sqrt(2)))
def circle_intersect_southwest():
    c = Circle(center=Point(2, 2), radius=1)
    return c.intersect_from_center(origin)

@testa.is_(expect=[
    Point(-1, 5),
    Point(3, 5),
    Point(3, -1),
    Point(-1, -1),
])
def rectangle_vertices():
    return Rectangle(center=Point(1, 2), width=4, height=6).vertices()

def rectangle_tb(case_f):
    for x in range(-2, 3):
        for y in range(-2, 3):
            c = Point(x, y)
            for w in range(1, 5):
                for h in range(1, 5):
                    res = case_f(c, w, h)
                    if res is not None:
                        return res

@testa.eq(
    oracle=lambda c,w,h: (c,w,h),
    testbench=rectangle_tb,
)
def rectangle_center_width_height(center, width, height):
    r = Rectangle(center=center, width=width, height=height)
    return (r.center(), r.width(), r.height())

@testa.eq(
    oracle=lambda c,w,h: Rectangle(center=c, width=w, height=h),
    testbench=rectangle_tb,
)
def rectangle_ctor_vertices(c, w, h):
    vertices = [
        c + Point(-w/2, h/2),
        c + Point(w/2, h/2),
        c + Point(w/2, -h/2),
        c + Point(-w/2, -h/2),
    ]
    return Rectangle(vertices=vertices)

@testa.is_(expect=Point(2, 3))
def rectangle_intersect_north():
    r = Rectangle(center=Point(2, 2), width=2, height=2)
    return r.intersect_from_center(Point(2, 4))

@testa.is_(expect=Point(3, 2))
def rectangle_intersect_east():
    r = Rectangle(center=Point(2, 2), width=2, height=2)
    return r.intersect_from_center(Point(4, 2))

@testa.is_(expect=Point(2, 1))
def rectangle_intersect_south():
    r = Rectangle(center=Point(2, 2), width=2, height=2)
    return r.intersect_from_center(Point(2, 0))

@testa.is_(expect=Point(1, 2))
def rectangle_intersect_west():
    r = Rectangle(center=Point(2, 2), width=2, height=2)
    return r.intersect_from_center(Point(0, 2))

@testa.is_(expect=Point(3, 3))
def rectangle_intersect_northeast():
    r = Rectangle(center=Point(2, 2), width=2, height=2)
    return r.intersect_from_center(Point(4, 4))

@testa.is_(expect=Point(3, 1))
def rectangle_intersect_southeast():
    r = Rectangle(center=Point(2, 2), width=2, height=2)
    return r.intersect_from_center(Point(4, 0))

@testa.is_(expect=Point(1, 1))
def rectangle_intersect_southwest():
    r = Rectangle(center=Point(2, 2), width=2, height=2)
    return r.intersect_from_center(Point(0, 0))

@testa.is_(expect=Point(1, 3))
def rectangle_intersect_northwest():
    r = Rectangle(center=Point(2, 2), width=2, height=2)
    return r.intersect_from_center(Point(0, 4))

@testa.is_(
    expect=[
        origin,
        Point(1, 3),
        Point(2, 0),
    ]
)
def triangle_ctor_cwh():
    return Triangle(center=Point(1, 1), width=2, height=3).vertices()

@testa.is_(expect=(Point(1, 1), 2, 3))
def triangle_ctor_vertices():
    vs = [
        origin,
        Point(1, 3),
        Point(2, 0),
    ]
    t = Triangle(vertices=vs)
    return (t.center(), t.width(), t.height())

@testa.is_(
    expect=[
        Arrow(src=origin, dst=Point(1, 3)),
        Arrow(src=Point(1, 3), dst=Point(2, 0)),
        Arrow(src=Point(2, 0), dst=origin),
    ]
)
def triangle_edges():
    vs = [
        origin,
        Point(1, 3),
        Point(2, 0),
    ]
    t = Triangle(vertices=vs)
    return t.edges()

def triangle_height_tb(case_f):
    ts = [Point(x, 1) for x in range(-1, 4)]
    l = origin
    r = Point(2, 0)
    for t in ts:
        res = case_f(l, t, r)
        if res is not None:
            return res

@testa.verify(
    trial=lambda l, t, r: Triangle(vertices=[l, t, r]).height(),
    testbench=triangle_height_tb,
)
def triangle_height_verifier(res, l, t, r):
    if fabs(res - 1) > 0.005:
        return 'expect 1.00 actual {:.2f} by applying ({}, {}, {})'.format(
            res, l, t, r)

@testa.is_(expect=Point(2, 1))
def triangle_intersect_south():
    t = Triangle(vertices=[Point(1, 1), Point(2, 4), Point(3, 1)])
    return t.intersect_from_center(Point(2, 0))

@testa.is_(expect=Point(2.67, 2))
def triangle_intersect_east():
    t = Triangle(vertices=[Point(1, 1), Point(2, 4), Point(3, 1)])
    return t.intersect_from_center(Point(3, 2))

@testa.is_(expect=Point(1.33, 2))
def triangle_intersect_west():
    t = Triangle(vertices=[Point(1, 1), Point(2, 4), Point(3, 1)])
    return t.intersect_from_center(Point(1, 2))

if __name__ == '__main__':
    testa.main()
