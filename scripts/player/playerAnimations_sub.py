
import pyxel

class playerAnimations():
    def checkPlayerAnimations(self):
        if ( self.player_is_alive and pyxel.frame_count % 20 == 1 ):
            if self.player_vy == 0:
                self.player_vy = 16
            else:
                self.player_vy = 0