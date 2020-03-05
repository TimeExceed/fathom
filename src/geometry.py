import math

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '({:.2f},{:.2f})'.format(self.x, self.y)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if math.fabs(self.x - other.x) >= 0.01:
            return False
        if math.fabs(self.y - other.y) >= 0.01:
            return False
        return True

    def center(self):
        return self

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

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

class Arrow(WithVertices):
    def __init__(self, from_pt, to_pt):
        assert type(from_pt) == Point, type(from_pt)
        assert type(to_pt) == Point, type(to_pt)
        self.from_pt = from_pt
        self.to_pt = to_pt

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.from_pt != other.from_pt:
            return False
        if self.to_pt != other.to_pt:
            return False
        return True

    def __repr__(self):
        return '({} to {})'.format(self.from_pt, self.to_pt)

    def length(self):
        p2 = self.from_pt - self.to_pt
        return math.sqrt(p2.x * p2.x + p2.y * p2.y)

    def vertices(self):
        return [self.from_pt, self.to_pt]

    def intersect_line(self, other_arr):
        norm_target = other_arr.to_pt - other_arr.from_pt
        norm_self = Arrow(
            self.from_pt - other_arr.from_pt,
            self.to_pt - other_arr.from_pt)
        intersected_pt = norm_self._intersect(norm_target)
        if intersected_pt is None:
            return None
        else:
            return intersected_pt + other_arr.from_pt

    def _intersect(self, target_pt):
        x0 = self.from_pt.x
        y0 = self.from_pt.y
        x1 = self.to_pt.x
        y1 = self.to_pt.y
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
        if Arrow(origin, target_pt)._inside(res) and self._inside(res):
            return res
        else:
            return None

    def _inside(self, pt):
        c = self.length()
        a = Arrow(pt, self.from_pt).length()
        b = Arrow(pt, self.to_pt).length()
        if a == 0 or b == 0:
            return True
        else:
            return (a*a + b*b - c*c) < 0

class Circle:
    def __init__(self, center, radius):
        assert type(center) == Point, type(center)
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

    def intersect_from_center(self, to_pt):
        p = to_pt - self.center()
        l = Arrow(origin, p).length()
        if l < self.radius:
            return None
        x = p.x * self.radius / l
        y = p.y * self.radius / l
        return Point(x, y) + self.center()

if __name__ == '__main__':
    p0 = Point(3, 4)
    p1 = Point(0, 0)
    l = Arrow(p0, p1)
    print(l.center())
