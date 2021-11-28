__all__ = ['Shape']

from abc import ABC, abstractmethod
from typing import Union, List
import fathom.geometry as geo
from .utils import *
from .opts import *
from .. import corner_styles

class Shape(ABC):
    def __init__(self, kws):
        self._pen_color = get_pen_color(kws)
        self._brush_color = get_brush_color(kws)
        self._line_style = get_line_style(kws)
        self._corner_style = get_corner_style(kws)

    def get_skeleton(self):
        return self._geo

    @abstractmethod
    def instructions(self, insts):
        pass
