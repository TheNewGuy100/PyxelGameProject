import pyxel


class playerClass():

    score = 0
    player_x = 72
    player_y = 16
    player_vy = 0
    player_is_alive = True

    def updatePlayer(self):
        self.checkPlayerHeight()
        self.checkPlayerDead()
        self.checkPlayerMovement()







    def checkPlayerMovement(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.player_x = max(self.player_x - 2, 0)

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)

    def checkPlayerHeight(self):
        if ( self.player_y < self.floor_collision):
            self.player_y += self.player_vy
            self.player_vy = min(self.player_vy + 1, 8)

    def checkPlayerDead(self):
        # PLAYER CHECK DEAD
        if self.player_y > pyxel.height:
            if self.player_is_alive:
                self.player_is_alive = False
                pyxel.play(3, 5)

            if self.player_y > 600:
                self.score = 0
                self.player_x = 72
                self.player_y = -16
                self.player_vy = 0
                self.player_is_alive = True
    
    def drawPlayer(self):
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            16 if self.player_vy > 0 else 0,
            0,
            16,
            16,
            12,
        )
