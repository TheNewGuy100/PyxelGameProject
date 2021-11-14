
import random
import pyxel

class ammoSpawner():
    probability = 0
    ammo_package_list = []
    ammo_package_x = 0
    ammo_package_y = 0
    ammo_package_img = 0
    ammo_package_u = 48
    ammo_package_v = 0
    ammo_package_w = 16
    ammo_package_h = 16
    ammo_package_color_exclusion = 0

    def spawnAmmoInMap(self):
        if pyxel.frame_count % 500 == 0 and pyxel.frame_count != 0:
            if random.randint(0,1) == 1:
                self.ammo_package_list.append({
                    "x": self.APP_X_MAX_PLAYABLE_AREA + 10,
                    "y": random.randint(self.APP_Y_MIN_PLAYABLE_AREA, self.APP_Y_MAX_PLAYABLE_AREA),
                    "img": self.ammo_package_img,
                    "u": self.ammo_package_u,
                    "v":  self.ammo_package_v,
                    "w": self.ammo_package_w,
                    "h": self.ammo_package_h,
                    "colkey": self.ammo_package_color_exclusion
            })

    def drawAmmoBox(self):
        if self.ammo_package_list.__len__() > 0:
            for index, ammo_box in enumerate(self.ammo_package_list):
                pyxel.blt(
                    ammo_box["x"],
                    ammo_box["y"],
                    ammo_box["img"],
                    ammo_box["u"],
                    ammo_box["v"],
                    ammo_box["w"],
                    ammo_box["h"],
                    ammo_box["colkey"]
                )
                ammo_box['x'] -= 1

            if abs(self.player_x-ammo_box['x']) <= 16 and abs(self.player_y-ammo_box['y']) <= 16:
                self.player_ammo += 40
                self.ammo_package_list.pop(index)
                pyxel.play(0, 4)
            if(ammo_box['x'] < self.APP_X_MIN_PLAYABLE_AREA):
                self.ammo_package_list.pop(index)

