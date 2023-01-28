import os
import time
from termcolor import colored

class Canvas: 
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [['' for y in range(self._y)] for x in range(self._x)]

    #def hitswall(self, point):
    #    return point[0] < 0 or point[0] >= self._x

canvas = Canvas(3, 3)

print(canvas._canvas)
