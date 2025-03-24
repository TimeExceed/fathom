from __future__ import annotations
import math
from itertools import cycle
from typing import *
from numbers import *
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def center(self):
        pass

class Point(Shape):
    def __init__(self, x: Real, y: Real) -> None:
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '({:.2f},{:.2f})'.format(self.x, self.y)

    def __eq__(self, other: Point) -> bool:
        if math.fabs(self.x - other.x) >= 0.005:
            return False
        if math.fabs(self.y - other.y) >= 0.005:
            return False
        return True

    def center(self):
        return self

    def copy(self):
        return Point(self.x, self.y)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Point) -> Point:
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other: Point) -> Point:
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, mul: float) -> Point:
        res = Point(self.x, self.y)
        res *= mul
        return res

    def __imul__(self, mul: float) -> Point:
        self.x *= mul
        self.y *= mul
        return self

    def __truediv__(self, div: float) -> Point:
        res = Point(self.x, self.y)
        res /= div
        return res

    def __itruediv__(self, div: float) -> Point:
        self.x /= div
        self.y /= div
        return self

ORIGIN = Point(0, 0)

def centroid(points: List[Point]) -> Point:
    assert len(points) > 0
    x = sum(p.x for p in points)
    y = sum(p.y for p in points)
    return Point(x/len(points), y/len(points))


class WithVertices(Shape):
    def vertices(self) -> List[Point]:
        raise NotImplementedError

    def center(self) -> Point:
        return centroid(self.vertices())

    def __eq__(self: VertexedT, other: VertexedT) -> bool:
        if type(self) != type(other):  # pylint: disable=unidiomatic-typecheck
            return False
        if self.vertices() != other.vertices():
            return False
        return True

    def edges(self) -> List[Arrow]:
        # pylint: disable=invalid-name
        vs = self.vertices()
        nvs = cycle(vs)
        next(nvs)
        return [Arrow(src=p0, dst=p1) for p0, p1 in zip(vs, nvs)]

    def intersect_from_center(self, target: Point) -> Optional[Point]:
        assert isinstance(target, Point), type(target)
        center_line = Arrow(src=self.center(), dst=target)
        for e in self.edges():
            res = center_line.intersect_line(e)
            if res is not None:
                return res
        return None


VertexedT = TypeVar('VertexedT', bound=WithVertices)


class Arrow(WithVertices):
    def __init__(self, **kws):
        src = kws['src']
        assert isinstance(src, Point), type(src)
        dst = kws['dst']
        assert isinstance(dst, Point), type(dst)
        self.src = src
        self.dst = dst

    def __repr__(self):
        return '({} to {})'.format(self.src, self.dst)

    def length(self) -> float:
        p2 = self.src - self.dst
        return math.sqrt(p2.x * p2.x + p2.y * p2.y)

    def vertices(self) -> List[Point]:
        return [self.src, self.dst]

    def intersect_line(self, other: Arrow) -> Optional[Point]:
        norm_target = other.dst - other.src
        norm_self = Arrow(
            src=self.src - other.src,
            dst=self.dst - other.src)
        intersected_pt = norm_self\
            .__intersect(norm_target)  # pylint: disable=protected-access
        if intersected_pt is None:
            return None
        return intersected_pt + other.src

    def __intersect(self, target_pt: Point) -> Optional[Point]:
        # pylint: disable=too-many-locals, protected-access
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
        if y1 * xx == x1 * yy:
            res = ORIGIN
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
        if Arrow(src=ORIGIN, dst=target_pt).__inside(res) and self.__inside(res):
            return res
        return None

    def __inside(self, pt: Point) -> bool:
        c = self.length()
        a = Arrow(src=pt, dst=self.src).length()
        b = Arrow(src=pt, dst=self.dst).length()
        if a == 0 or b == 0:
            return True
        return (a*a + b*b - c*c) < 0

class Circle(Shape):
    def __init__(self, **kws):
        center = kws['center']
        assert isinstance(center, Point), type(center)
        radius = kws['radius']
        assert radius > 0, radius
        self._center = center
        self.radius = float(radius)

    def __repr__(self):
        return '(Circle center={} radius={})'.format(self._center, self.radius)

    def __eq__(self, other: Circle) -> bool:
        if self._center != other._center:
            return False
        if self.radius != other.radius:
            return False
        return True

    def center(self) -> Point:
        return self._center

    def intersect_from_center(self, dst: Point) -> Optional[Point]:
        p = dst - self.center()
        l = Arrow(src=ORIGIN, dst=p).length()
        if l < self.radius:
            return None
        x = p.x * self.radius / l
        y = p.y * self.radius / l
        return Point(x, y) + self.center()

class Rectangle(WithVertices):
    def __init__(self, **kws):
        if 'center' in kws:
            center = kws['center']
            assert isinstance(center, Point), type(center)
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
        elif 'lower_left' in kws and 'upper_right' in kws:
            lower_left = kws['lower_left']
            upper_right = kws['upper_right']
            self._vertices = [
                Point(lower_left.x, upper_right.y),
                upper_right,
                Point(upper_right.x, lower_left.y),
                lower_left,
            ]
        else:
            assert 'vertices' in kws
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

    def vertices(self) -> List[Point]:
        return self._vertices

    def width(self) -> float:
        vertices = self.vertices()
        return Arrow(src=vertices[1], dst=vertices[0]).length()

    def height(self) -> float:
        vertices = self.vertices()
        return Arrow(src=vertices[1], dst=vertices[2]).length()

class Triangle(WithVertices):
    def __init__(self, **kws):
        vertices = kws.get('vertices')
        if vertices is not None:
            self._vertices = vertices
        else:
            center = kws['center']
            assert isinstance(center, Point), type(center)
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

    def vertices(self) -> List[Point]:
        return self._vertices

    def width(self) -> float:
        vs = self.vertices()
        return Arrow(src=vs[0], dst=vs[2]).length()

    def height(self) -> float:
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
            assert isinstance(x, Point), type(x)
        self._vertices = vertices

    def __repr__(self):
        return '(Polygon corners=[{}])'.format(
            ', '.join('{}'.format(self.vertices())))

    def vertices(self) -> List[Point]:
        return self._vertices

class Diamond(WithVertices):
    def __init__(self, **kws) -> None:
        if 'center' in kws and 'width' in kws and 'height' in kws:
            center = kws['center']
            assert isinstance(center, Point), type(center)
            half_width = Point(kws['width'] / 2, 0)
            half_height = Point(0, kws['height'] / 2)
            left = center - half_width
            top = center + half_height
            right = center + half_width
            bottom = center - half_height
            self._vertices = [left, top, right, bottom]
        elif 'left' in kws and 'top' in kws:
            left = kws['left']
            assert isinstance(left, Point), type(left)
            top = kws['top']
            assert isinstance(top, Point), type(top)
            right = Point(top.x + (top.x - left.x), left.y)
            bottom = Point(top.x, left.y - (top.y - left.y))
            self._vertices = [left, top, right, bottom]
        else:
            assert 'vertices' in kws
            vs = kws['vertices']
            assert vs[0].x < vs[1].y, ' '.join([repr(x) for x in vs])
            assert vs[1].x == vs[3].x, ' '.join([repr(x) for x in vs])
            assert vs[1].x < vs[2].x, ' '.join([repr(x) for x in vs])
            assert vs[3].y < vs[0].y, ' '.join([repr(x) for x in vs])
            assert vs[0].y == vs[2].y, ' '.join([repr(x) for x in vs])
            assert vs[0].y < vs[1].y, ' '.join([repr(x) for x in vs])
            self._vertices = vs

    def __repr__(self) -> str:
        return '(Diamond corners=[{}])'.format(
            ', '.join('{}'.format(self.vertices())))

    def vertices(self) -> List[Point]:
        return self._vertices
