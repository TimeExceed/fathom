from __future__ import annotations
from typing import *

# pylint: disable=too-few-public-methods

class _InvisibleColor:
    def __init__(self):
        pass

    def __repr__(self):
        return 'invisible'


INVISIBLE = _InvisibleColor()


class _PredefinedColor:
    def __init__(self, pred):
        self._predefined = pred

    def __repr__(self):
        return self._predefined

    def scale(self, ratio):
        return _ScaledColor(self, ratio)

    def mix(self, other: Union[_PredefinedColor, _ScaledColor]) -> _MixedColor:
        return _MixedColor([self, other])


BLACK = _PredefinedColor('black')
WHITE = _PredefinedColor('white')
RED = _PredefinedColor('red')
GREEN = _PredefinedColor('green')
BLUE = _PredefinedColor('blue')
CYAN = _PredefinedColor('cyan')
MAGENTA = _PredefinedColor('magenta')
YELLOW = _PredefinedColor('yellow')
GRAY = _PredefinedColor('gray')
DARK_GRAY = _PredefinedColor('darkgray')
LIGHT_GRAY = _PredefinedColor('lightgray')
BROWN = _PredefinedColor('brown')
LIME = _PredefinedColor('lime')
OLIVE = _PredefinedColor('olive')
ORAGNE = _PredefinedColor('orange')
PINK = _PredefinedColor('pink')
PURPLE = _PredefinedColor('purple')
TEAL = _PredefinedColor('teal')
VIOLET = _PredefinedColor('violet')


class _ScaledColor:
    def __init__(self, base, ratio):
        self._base = base
        self._ratio = ratio

    def __repr__(self):
        return '{}!{:.0f}'.format(self._base, self._ratio)

    def mix(self, other: Union[_PredefinedColor, _ScaledColor]) -> _MixedColor:
        return _MixedColor([self, other])


class _MixedColor:
    def __init__(self, mixes):
        self._mixes = mixes

    def __repr__(self):
        return '!'.join(['{}'.format(x) for x in self._mixes])

    def mix(self, other: Union[_PredefinedColor, _ScaledColor]) -> _MixedColor:
        mixes = self._mixes[:]
        mixes.append(other)
        return _MixedColor(mixes)
