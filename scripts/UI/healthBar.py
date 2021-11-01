

import pyxel


class healthBarStatus():
    health = 100
    def updateHealthBar(self):
        healthDraw = "HEALTH: {:>4}".format(self.health)
        pyxel.text(5, 4, healthDraw, 1)
        pyxel.text(5, 4, healthDraw, 7)
