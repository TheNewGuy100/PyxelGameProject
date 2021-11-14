
import pyxel

class bulletsController():
    bullet_y = 0
    bullet_img = 0
    bullet_u = 96
    bullet_v = 0
    bullet_width = 16
    bullet_heigth = 16
    bullet_color_removed = 0,
    bullets_list = []
    bullet_speed = 2
    bullet_alignment = 10
    player_ammo = 60

    def createBullet(self, x, y):
        self.bullet_x = x
        self.bullet_y = y

        self.bullets_list.append({
            "x": self.bullet_x + self.bullet_alignment,
            "y": self.bullet_y,
            "img": 0,
            "u": 96,
            "v": 0,
            "w": 16,
            "h": 16,
            "colkey": 0,
        })
        self.player_ammo -= 1
        pyxel.play(0, 0)

    def drawBullets(self):
        if self.bullets_list.__len__() > 0:
            for bullet in self.bullets_list:
                    pyxel.blt(
                        bullet['x'],
                        bullet['y'],
                        bullet['img'],
                        bullet['u'],
                        bullet['v'],
                        bullet['w'],
                        bullet['h'],
                        bullet['colkey']
                    )

    def updateBullet(self):
        if self.bullets_list.__len__() > 0:
            for index, bullet in enumerate(self.bullets_list):
                bullet['x'] += self.bullet_speed
                if self.enemys_list.__len__() > 0:
                    for enemy_index, enemy in enumerate(self.enemys_list):
                        if abs(enemy['y']-bullet['y']) < 16 and abs(bullet['x']-enemy['x']) < 8:
                            self.enemys_list.pop(enemy_index)
                            self.bullets_list.pop(index)
                            self.score += 100
                            pyxel.play(0,3)

                if bullet['x'] > self.APP_X_MAX_PLAYABLE_AREA:
                    self.bullets_list.pop(index)
