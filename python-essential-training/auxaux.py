def draw(self, pos):
    self.canvas.setPos(self.pos, self.trail)
    self.pos = pos
    self.canvas.setPos(self.pos, colored(self.mark, 'red'))
    self.canvas.print()
    time.sleep(self.framerate)   
