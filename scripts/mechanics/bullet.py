
import pyxel


class Bullet():
    def storeBulletInfo(self, x, y):
        self.bullet_x = x
        self.bullet_y = y
        self.bullet_w = self.BULLET_WIDTH
        self.bullet_h = self.BULLET_HEIGHT
        self.alive = True

        self.bullets_list.append(self)
        self.draw(True)

    def updateBullet(self):
        self.bullet_y -= self.BULLET_SPEED

        if self.bullet_y + self.bullet_h - 1 < 0:
            self.alive = False