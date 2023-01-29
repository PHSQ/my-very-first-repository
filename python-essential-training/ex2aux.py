
import os
#from pprint import pprint

#EXEMPLO CRIADO PELO CHATGPT PARA EU APRENDER A USAR O setPos
#APROVEITEI E APRENDI A INSTANCIA CLEAR PELO CHATGPT3
#E DE QUEBRA A COMO USAR O pprint PARA IMPRIMIR UMA MATRIX DE FORMA MAIS BONITA

class MyCanvas:
    def __init__(self, width, height):
        self._canvas = [[' ' for _ in range(width)] for _ in range(height)]
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark
    def clear(self):
        os.system('clear')
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

canvas = MyCanvas(5, 5)
canvas.clear()
canvas.setPos((3, 3), 'X')
#print(canvas._canvas)

