
import pyxel

class drawPlayerInit():
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