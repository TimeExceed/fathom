class _Location:
    def __init__(self, loc):
        self._loc = loc

    def __repr__(self):
        return self._loc

CENTER = _Location('center')
NORTH = _Location('above')
SOUTH = _Location('below')
WEST = _Location('left')
EAST = _Location('right')
NORTHEAST = _Location('above right')
SOUTHEAST = _Location('below right')
SOUTHWEST = _Location('below left')
NORTHWEST = _Location('above left')
