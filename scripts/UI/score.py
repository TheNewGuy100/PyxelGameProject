
import pyxel


class scoreClass():
    score = 0
    def drawScore(self):
        s = "SCORE: {:>4}".format(self.score)
        pyxel.text(70, 4, s, 1)
        pyxel.text(70, 4, s, 7)