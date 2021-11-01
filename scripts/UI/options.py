
import pyxel

class optionsClass():

    def checkMenuOptions(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        