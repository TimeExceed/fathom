from fathom.geometry import Point
from . import colors
from . import line_styles


def format_point(pt):
    assert isinstance(pt, Point), type(pt)
    return '({},{})'.format(
        format_float(pt.x),
        format_float(pt.y))


def format_float(fp):
    return '{:.2f}cm'.format(fp)


def get_pen_color(kws):
    return kws.get('pen_color', colors.BLACK)


def get_brush_color(kws):
    return kws.get('brush_color', colors.INVISIBLE)


def get_line_style(kws):
    return kws.get('line_style', line_styles.SOLID)

def get_rounded_corner(kws):
    rc = kws.get('rounded_corner', None)
    if rc is None:
        return None
    if rc == 'default':
        return 0.15
    assert isinstance(rc, number), type(rc)
    return rc

def draw_cmd(shape, additional_opts=None):
    if shape._pen_color is colors.INVISIBLE:
        return None

    opts = []

    if additional_opts is not None:
        opts.extend(additional_opts)

    if shape._pen_color is not colors.BLACK:
        opts.append('color={}'.format(shape._pen_color))

    if shape._line_style is not line_styles.SOLID:
        opts.append('{}'.format(shape._line_style))

    if len(opts) == 0:
        return r'\draw'
    else:
        return r'\draw[{}]'.format(','.join(opts))


def fill_cmd(shape, additional_opts=None):
    if shape._brush_color is colors.INVISIBLE:
        return None

    opts = []

    if additional_opts is not None:
        opts.extend(additional_opts)

    if shape._brush_color is not colors.BLACK:
        opts.append('color={}'.format(shape._brush_color))

    if len(opts) == 0:
        return r'\fill'
    else:
        return r'\fill[{}]'.format(','.join(opts))
