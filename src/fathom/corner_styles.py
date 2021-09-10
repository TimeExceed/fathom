__all__ = ['SHARP', 'Rounded', 'DEFAULT_ROUNDED']

# pylint: disable=too-few-public-methods

class _Sharp:
    pass


SHARP = _Sharp()


class Rounded:
    def __init__(self, radius):
        self.radius = radius

DEFAULT_ROUNDED = Rounded(0.15)
