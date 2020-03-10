from .utils import format_length

# pylint: disable=too-few-public-methods

class _Sharp:
    pass


SHARP = _Sharp()


class Rounded:
    def __init__(self, radius):
        self._radius = radius

    def __repr__(self):
        return 'rounded corners={}'.format(format_length(self._radius))


DEFAULT_ROUNDED = Rounded(0.15)
