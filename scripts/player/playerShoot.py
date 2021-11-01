
from scripts.mechanics.bullet import Bullet

class playerShootController(
    Bullet
):
    BULLET_WIDTH = 2
    BULLET_HEIGHT = 8
    BULLET_COLOR = 10
    BULLET_SPEED = 4

    bullets_list = []
    player_ammo = 60

    def createBullet(self):
        self.storeBulletInfo( self.player_x - self.BULLET_WIDTH / 2, self.player_y - self.BULLET_HEIGHT / 2 )