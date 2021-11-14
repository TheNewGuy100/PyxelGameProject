

import pyxel


class playerCheckDead():
    def checkPlayerDead(self):
        for index, enemy in enumerate(self.enemys_list):
            if abs(enemy['y']-self.player_y) < 16 and abs(self.player_x-enemy['x']) < 8:
                self.enemys_list.pop(index)
                self.health -= 25
                pyxel.play(0,5)

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