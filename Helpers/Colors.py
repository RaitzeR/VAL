# -*- coding: utf-8 -*-
from typing import Tuple

COLORS = {'white': (255, 255, 255), 'red': (255, 0, 0), 'blue': (0, 0, 255), 'silver': (192, 192, 192),
          'black': (0, 0, 0)}


def getColor(color: str) -> Tuple[int, int, int]:
    return COLORS[color]
