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
    pen_color = kws.get('pen_color')
    if pen_color is not None:
        return pen_color
    return colors.BLACK


def get_brush_color(kws):
    brush_color = kws.get('brush_color')
    if brush_color is not None:
        return brush_color
    return colors.INVISIBLE


def get_line_style(kws):
    line_style = kws.get('line_style')
    if line_style is not None:
        return line_style
    return line_styles.SOLID


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
        return r'\draw[{opts}]'.format(opts=','.join(opts))


def fill_cmd(shape):
    if shape._brush_color is colors.INVISIBLE:
        return None

    if shape._brush_color is colors.BLACK:
        return r'\fill'
    else:
        return r'\fill[color={}]'.format(shape._brush_color)
