import os
import time
from termcolor import colored
#importa 3 modules

class Canvas:

    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]
    # It defines some height and width 

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y
    # Uma maneira de verificar se o ponto (point[0],point[1]) esta fora do grid (self._x,self._y)

canva = Canvas(2, 2)
a = Canvas(4,4)
estafora = Canvas.hitsWall(a,[5,3])

print(canva._canvas)
print(a._canvas)
print(estafora)