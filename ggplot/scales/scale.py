from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

class scale(object):
    """
    Base class for scales.
    """
    VALID_SCALES = []
    def __init__(self, *args, **kwargs):
        for s in self.VALID_SCALES:
            setattr(self, s, None)

        if args:
            self.name = args[0]

        for k, v in kwargs.items():
            if k in self.VALID_SCALES:
                setattr(self, k, v)
