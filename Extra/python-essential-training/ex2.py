import os
import time
from termcolor import colored
#importa 3 modules

class Canvas:

    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)] 
    #cria uma matrix de ' '

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y
    # Uma maneira de verificar se o ponto (point[0],point[1]) esta fora do grid (self._x,self._y)

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark
    # Coloca um marcador na posição na posicao indicada

    def clear(self):
        os.system('clear')
    #limpa o terminal

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))
            
    #limpa o terminal e imprime cada linha separadamente no canvas


a = Canvas(4,4)
a.print()