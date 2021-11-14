
import random
import pyxel

class medkitSpawner():
    probability = 0
    medkit_package_list = []
    medkit_package_x = 0
    medkit_package_y = 0
    medkit_package_img = 0
    medkit_package_u = 32
    medkit_package_v = 0
    medkit_package_w = 16
    medkit_package_h = 16
    medkit_package_color_exclusion = 0

    def spawnMedkitInMap(self):
        if pyxel.frame_count % 750 == 0 and pyxel.frame_count != 0:
            if random.randint(0,1) == 1:
                self.medkit_package_list.append({
                    "x": self.APP_X_MAX_PLAYABLE_AREA + 10,
                    "y": random.randint(self.APP_Y_MIN_PLAYABLE_AREA, self.APP_Y_MAX_PLAYABLE_AREA),
                    "img": self.medkit_package_img,
                    "u": self.medkit_package_u,
                    "v":  self.medkit_package_v,
                    "w": self.medkit_package_w,
                    "h": self.medkit_package_h,
                    "colkey": self.medkit_package_color_exclusion
            })

    def drawMedkitBox(self):
        if self.medkit_package_list.__len__() > 0:
            for index, medkit_box in enumerate(self.medkit_package_list):
                pyxel.blt(
                    medkit_box["x"],
                    medkit_box["y"],
                    medkit_box["img"],
                    medkit_box["u"],
                    medkit_box["v"],
                    medkit_box["w"],
                    medkit_box["h"],
                    medkit_box["colkey"]
                )
                medkit_box['x'] -= 1

            if abs(self.player_x-medkit_box['x']) <= 16 and abs(self.player_y-medkit_box['y']) <= 16:
                if self.health < 100:
                    self.health += 25
                self.medkit_package_list.pop(index)
                pyxel.play(0, 4)
            if(medkit_box['x'] < self.APP_X_MIN_PLAYABLE_AREA):
                self.medkit_package_list.pop(index)

