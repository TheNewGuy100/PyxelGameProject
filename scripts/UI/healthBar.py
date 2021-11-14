

import pyxel


class healthBarStatus():
    health = 100
    def drawHealthBar(self):
        healthDraw = "HEALTH: {:>4}".format(self.health)
        pyxel.text(2, 2, healthDraw, 8)
    
    def checkHealth(self):
        if self.health == 0:
            self.player_is_alive = False
