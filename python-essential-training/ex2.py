import os
import time
from termcolor import colored
#importa 3 modules

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]
# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving

canva = Canvas(2, 2)
print(canva._canvas)