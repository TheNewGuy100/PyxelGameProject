

import pyxel


class playerCheckDead():
    def checkPlayerDead(self):
        if self.health == 0:
            if self.player_is_alive:
                self.player_is_alive = False
                pyxel.play(3, 5)

            if self.player_is_alive == False:
                self.score = 0
                self.player_x = 72
                self.player_y = -16
                self.player_vy = 0
                self.player_is_alive = True