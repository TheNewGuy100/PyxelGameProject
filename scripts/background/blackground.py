from random import randint

import pyxel

class BackgroundClass():
    far_cloud = [(-10, 20), (40, 40), (90, 60)]
    near_cloud = [(-10, 75), (90, 65), (150, 60)]

    def drawBackground(self):
        offset = (pyxel.frame_count // 4) % 60

        for i in range(2):
            pyxel.blt(i * 160 - offset, 0, 0, 0, 56, 160, 80)

        for i in range(2):
            pyxel.blt(i * 160 - offset, 80, 0, 0, 56, 160, 50)
        

    def updateBackground(self):

        return