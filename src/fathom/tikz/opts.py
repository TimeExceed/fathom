from typing import Union
from . import colors
from . import line_styles
from . import corner_styles
from .utils import *

# pylint: disable=protected-access


def get_pen_color(kws) -> Union[colors._InvisibleColor,
                                colors._PredefinedColor,
                                colors._ScaledColor,
                                colors._MixedColor]:
    return kws.get('pen_color', colors.BLACK)


def get_brush_color(kws) -> Union[colors._InvisibleColor,
                                  colors._PredefinedColor,
                                  colors._ScaledColor,
                                  colors._MixedColor]:
    return kws.get('brush_color', colors.INVISIBLE)


def get_line_style(kws) -> line_styles._LineStyle:
    return kws.get('line_style', line_styles.SOLID)


def get_corner_style(kws) -> Union[corner_styles._Sharp, corner_styles.Rounded]:
    return kws.get('corner_style', corner_styles.SHARP)


def draw_cmd(shape, additional_opts=None) -> str:
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
    return r'\draw[{}]'.format(','.join(opts))


def fill_cmd(shape, additional_opts=None) -> str:
    if shape._brush_color is colors.INVISIBLE:
        return None

    opts = []

    if additional_opts is not None:
        opts.extend(additional_opts)

    if shape._brush_color is not colors.BLACK:
        opts.append('color={}'.format(shape._brush_color))

    if len(opts) == 0:
        return r'\fill'
    return r'\fill[{}]'.format(','.join(opts))
