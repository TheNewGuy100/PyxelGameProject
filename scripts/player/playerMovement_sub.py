
import pyxel

class playerMovement():
        def checkPlayerMovement(self):

            if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
                self.player_x = max(self.player_x - 2, 0)

            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
                self.player_x = min(self.player_x + 2, pyxel.width - 16)

            if not (  self.player_y == self.APP_HEIGHT + 12  or self.player_y == 0):
                if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.GAMEPAD_1_UP):
                    self.player_y = min(self.player_y - 1, pyxel.height - 1)

            if not (  self.player_y == self.APP_HEIGHT - 12  or self.player_y == 0):
                if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
                    self.player_y = min(self.player_y + 1, pyxel.height + 1)

            # SAFE-MEASURES
            if self.player_y >= self.APP_HEIGHT:
                self.player_y -= 1

            if self.player_y <= self.APP_HEIGHT - self.APP_HEIGHT:
                self.player_y += 1

            if self.player_x >= self.APP_WIDTH:
                self.player_x -= 1

            if self.player_x <= self.APP_WIDTH - self.APP_WIDTH:
                self.player_x += 1
