from fathom.geometry import Point

def format_point(pt: Point) -> str:
    assert isinstance(pt, Point), type(pt)
    return '({},{})'.format(
        format_length(pt.x),
        format_length(pt.y))


def format_length(fp: float) -> str:
    return '{:.2f}cm'.format(fp)

def default_construct_shape(cls, args, kws):
    shape = check_geoshape_in_args(cls, args)
    if shape:
        return shape
    return cls(**kws)

def check_geoshape_in_args(cls, args):
    if len(args) > 0:
        assert len(args) == 1
        assert isinstance(args[0], cls)
        return args[0]
    else:
        return None