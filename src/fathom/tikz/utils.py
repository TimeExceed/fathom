from fathom.geometry import Point

def format_point(pt: Point) -> str:
    assert isinstance(pt, Point), type(pt)
    return '({},{})'.format(
        format_length(pt.x),
        format_length(pt.y))


def format_length(fp: float) -> str:
    return '{:.2f}cm'.format(fp)
