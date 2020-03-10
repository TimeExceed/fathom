from .utils import format_length

SHARP = object()

class Rounded:
    def __init__(self, radius):
        self._radius = radius

    def __repr__(self):
        return 'rounded corners={}'.format(format_length(self._radius))

DEFAULT_ROUNDED = Rounded(0.15)
