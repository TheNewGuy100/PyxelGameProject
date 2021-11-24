
import pyxel

class playerMovement():
    shoot_delay = 0

    def checkPlayerMovement(self):

        # LEFT
        if self.player_x >= self.APP_X_MIN_PLAYABLE_AREA:
            if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
                self.player_x = max(self.player_x - 2, 0)

        # RIGHT
        if self.player_x <= self.APP_X_MAX_PLAYABLE_AREA:
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
                self.player_x = min(self.player_x + 2, pyxel.width - 2)

        # UP
        if self.player_y >= self.APP_Y_MIN_PLAYABLE_AREA:
            if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.GAMEPAD_1_UP):
                self.player_y = min( self.player_y - 2, pyxel.height - 2)

        # DOWN
        if self.player_y <= self.APP_Y_MAX_PLAYABLE_AREA:
            if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
                self.player_y = min( self.player_y + 2, pyxel.height + 2)

        # SHOOT
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_B) and self.player_ammo > 0:
            if ( pyxel.frame_count >= self.shoot_delay ):
                self.createBullet(self.player_x, self.player_y)
                self.shoot_delay = pyxel.frame_count + 10