

import pyxel


class ammoBar():
    def drawAmmoBar(self):
        ammoBar = "AMMO: {:>4}".format(self.player_ammo)
        pyxel.text(55, 2, ammoBar, 0)
