from dataclasses import dataclass


@dataclass
class Point:
    """ A simple 2d point with integer coordinates"""

    x: int = 0
    y: int = 0


TIMEOUT_60FPS : float = 0.016