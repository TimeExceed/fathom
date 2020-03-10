class _LineStyle:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return self._name


DASHED = _LineStyle('dashed')
DOTTED = _LineStyle('dotted')
SOLID = _LineStyle('solid')
