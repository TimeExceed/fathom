import math
from itertools import cycle

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '({:.2f},{:.2f})'.format(self.x, self.y)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if math.fabs(self.x - other.x) >= 0.005:
            return False
        if math.fabs(self.y - other.y) >= 0.005:
            return False
        return True

    def center(self):
        return self

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

origin = Point(0, 0)

def centroid(points):
    assert len(points) > 0
    x = sum(p.x for p in points)
    y = sum(p.y for p in points)
    return Point(x/len(points), y/len(points))

class WithVertices:
    def vertices(self):
        raise NotImplementedError

    def center(self):
        return centroid(self.vertices())

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.vertices() != other.vertices():
            return False
        return True

    def edges(self):
        vs = self.vertices()
        nvs = cycle(vs)
        next(nvs)
        return [Arrow(src=p0, dst=p1) for p0, p1 in zip(vs, nvs)]

    def intersect_from_center(self, target):
        assert type(target) == Point, type(target)
        center_line = Arrow(src=self.center(), dst=target)
        for e in self.edges():
            res = center_line.intersect_line(e)
            if res is not None:
                return res

class Arrow(WithVertices):
    def __init__(self, **kws):
        src = kws['src']
        assert type(src) == Point, type(src)
        dst = kws['dst']
        assert type(dst) == Point, type(dst)
        self.src = src
        self.dst = dst

    def __repr__(self):
        return '({} to {})'.format(self.src, self.dst)

    def length(self):
        p2 = self.src - self.dst
        return math.sqrt(p2.x * p2.x + p2.y * p2.y)

    def vertices(self):
        return [self.src, self.dst]

    def intersect_line(self, other_arr):
        norm_target = other_arr.dst - other_arr.src
        norm_self = Arrow(
            src=self.src - other_arr.src,
            dst=self.dst - other_arr.src)
        intersected_pt = norm_self._intersect(norm_target)
        if intersected_pt is None:
            return None
        else:
            return intersected_pt + other_arr.src

    def _intersect(self, target_pt):
        x0 = self.src.x
        y0 = self.src.y
        x1 = self.dst.x
        y1 = self.dst.y
        x2 = target_pt.x
        y2 = target_pt.y
        xx = x1 - x0
        yy = y1 - y0
        if xx * y2 == x2 * yy:
            return None
        elif y1 * xx == x1 * yy:
            res = origin
        else:
            a = (y1 - y0) / (x0 * y1 - x1 * y0)
            b = (x1 - x0) / (x1 * y0 - x0 * y1)
            if x2 == 0:
                res = Point(0, 1/b)
            else:
                c = y2 / x2
                x = 1 / (b * c + a)
                y = x * c
                res = Point(x, y)
        if Arrow(src=origin, dst=target_pt)._inside(res) and self._inside(res):
            return res
        else:
            return None

    def _inside(self, pt):
        c = self.length()
        a = Arrow(src=pt, dst=self.src).length()
        b = Arrow(src=pt, dst=self.dst).length()
        if a == 0 or b == 0:
            return True
        else:
            return (a*a + b*b - c*c) < 0

class Circle:
    def __init__(self, **kws):
        center = kws['center']
        assert type(center) == Point, type(center)
        radius = kws['radius']
        assert radius > 0, radius
        self._center = center
        self.radius = float(radius)

    def __repr__(self):
        return '(Circle center={} radius={})'.format(self._center, self.radius)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self._center != other._center:
            return False
        if self.radius != other.radius:
            return False
        return True

    def center(self):
        return self._center

    def intersect_from_center(self, dst):
        p = dst - self.center()
        l = Arrow(src=origin, dst=p).length()
        if l < self.radius:
            return None
        x = p.x * self.radius / l
        y = p.y * self.radius / l
        return Point(x, y) + self.center()

class Rectangle(WithVertices):
    def __init__(self, **kws):
        center = kws.get('center')
        if center is not None:
            assert type(center) == Point, type(center)
            width = kws['width']
            assert width > 0, width
            height = kws['height']
            assert height > 0, height
            half_width = float(width) / 2
            half_height = float(height) / 2
            corners = [
                Point(-half_width, half_height),
                Point(half_width, half_height),
                Point(half_width, -half_height),
                Point(-half_width, -half_height),
            ]
            self._vertices = [p + center for p in corners]
        else:
            vertices = kws['vertices']
            top = Arrow(src=vertices[0], dst=vertices[1]).length()
            bottom = Arrow(src=vertices[2], dst=vertices[3]).length()
            assert top == bottom, 'top={:.2f} bottom={:.2f}'.format(top, bottom)
            left = Arrow(src=vertices[0], dst=vertices[3]).length()
            right = Arrow(src=vertices[2], dst=vertices[1]).length()
            assert left == right, 'left={:.2f} right={:.2f}'.format(left, right)
            diagonal = Arrow(src=vertices[1], dst=vertices[3]).length()
            assert math.fabs(top*top + left*left - diagonal*diagonal) < 0.005,\
                'left={:.2f} top={:.2f} diagonal={:.2f}'.format(left, top, diagonal)
            self._vertices = vertices

    def __repr__(self):
        return '(Rectangle center={} width={:.2f} height={:.2f})'.format(
            self.center(),
            self.width(),
            self.height(),
        )

    def vertices(self):
        return self._vertices

    def width(self):
        vertices = self.vertices()
        return Arrow(src=vertices[1], dst=vertices[0]).length()

    def height(self):
        vertices = self.vertices()
        return Arrow(src=vertices[1], dst=vertices[2]).length()

class Triangle(WithVertices):
    def __init__(self, **kws):
        vertices = kws.get('vertices')
        if vertices is not None:
            self._vertices = vertices
        else:
            center = kws['center']
            assert type(center) == Point, type(center)
            width = float(kws['width'])
            assert width > 0, width
            height = float(kws['height'])
            assert height > 0, height
            corners = [
                Point(-width / 2, -height / 3),
                Point(0, height * 2 / 3),
                Point(width / 2, -height / 3),
            ]
            self._vertices = [(center + x) for x in corners]

    def __repr__(self):
        return '(Triangle corners=[{}])'.format(
            ', '.join('{}'.format(self.vertices())))

    def vertices(self):
        return self._vertices

    def width(self):
        vs = self.vertices()
        return Arrow(src=vs[0], dst=vs[2]).length()

    def height(self):
        es = self.edges()
        a = es[0].length()
        b = es[2].length()
        c = es[1].length()
        cos_gammar = (a * a + b * b - c * c) / (2 * a * b)
        cos_gammar_sqr = cos_gammar * cos_gammar
        sin_gammar = math.sqrt(1 - cos_gammar_sqr)
        return a * sin_gammar

class Polygon(WithVertices):
    def __init__(self, **kws):
        vertices = kws['vertices']
        vertices = list(vertices)
        for x in vertices:
            assert type(x) == Point, type(x)
        self._vertices = vertices

    def __repr__(self):
        return '(Polygon corners=[{}])'.format(
            ', '.join('{}'.format(self.vertices())))

    def vertices(self):
        return self._vertices