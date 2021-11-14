
import pyxel

class scoreClass():
    score = 0
    def drawScore(self):
        s = "SCORE: {:>4}".format(self.score)
        pyxel.text(2, 10, s, 0)