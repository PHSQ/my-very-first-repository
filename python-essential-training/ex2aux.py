#EXEMPLO CRIADO PELO CHATGPT PARA EU APRENDER A USAR O setPos

class MyCanvas:
    def __init__(self, width, height):
        self._canvas = [[' ' for _ in range(width)] for _ in range(height)]
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

canvas = MyCanvas(5, 5)
canvas.setPos((3, 3), 'X')
print(canvas._canvas)

