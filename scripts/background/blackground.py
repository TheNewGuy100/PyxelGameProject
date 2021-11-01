
import pyxel

class BackgroundClass():

    def drawBackground(self):
        offset = pyxel.frame_count % 60

        for i in range(2):
            pyxel.blt(i * 160 - offset, 0, 0, 0, 32, 160, 120)

        for i in range(2):
            pyxel.blt(i * 160 - offset, 105, 0, 0, 56, 160, 50)
        

    def updateBackground(self):

        return