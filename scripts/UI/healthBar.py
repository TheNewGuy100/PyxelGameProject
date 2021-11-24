

import pyxel


class healthBarStatus():
    health = 100
    enableGameOver = False
    color = 7
    color_types = {
        "7": 0,
        "0": 7
    }

    def drawHealthBar(self):
        healthDraw = "HEALTH: {:>4}".format(self.health)
        pyxel.text(2, 2, healthDraw, 8)
    
    def checkHealth(self):
        if self.health <= 0:
            self.player_is_alive = False

    def gameOverCheck(self):
        if self.enableGameOver == True:
            pyxel.text(
                self.APP_WIDTH/2 - 16,
                self.APP_HEIGHT/2 - 8,
                "GAME OVER",
                self.color
            )
            if (pyxel.frame_count % 20 == 1):
                self.color = self.color_types[self.color.__str__()]
