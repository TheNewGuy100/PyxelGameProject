from random import randint

import pyxel

class BackgroundClass():
    far_cloud = [(-10, 75), (40, 65), (90, 60)]
    near_cloud = [(10, 25), (70, 35), (120, 15)]
    floor_height = 104
    floor_collision = 104 - 20

    def drawBackground(self):
        # draw sky
        pyxel.blt(0, 88, 0, 0, 88, 160, 32)

        # draw mountain
        pyxel.blt(0, 88, 0, 0, 64, 160, 24, 12)

        # draw forest
        offset = pyxel.frame_count % 160
        for i in range(2):
            pyxel.blt(i * 160 - offset, 104, 0, 0, 48, 160, 16, 12)

        # draw clouds
        offset = (pyxel.frame_count // 16) % 160
        for i in range(2):
            for x, y in self.far_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 64, 32, 32, 8, 12)

        offset = (pyxel.frame_count // 8) % 160
        for i in range(2):
            for x, y in self.near_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 56, 8, 12)

        # draw floors
            pyxel.blt(i * 160 - offset, self.floor_height, 0, 0, 16, 160, 16, 12)
        

    def updateBackground(self):

        return