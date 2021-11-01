

import pyxel


class healthBarStatus():
    health = 100
    def drawHealthBar(self):
        healthDraw = "HEALTH: {:>4}".format(self.health)
        pyxel.text(5, 4, healthDraw, 1)
        pyxel.text(5, 4, healthDraw, 7)
    
    def checkHealth(self):
        if self.health == 0:
            self.player_is_alive = False
