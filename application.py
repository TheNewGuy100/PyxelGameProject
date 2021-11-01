
import pyxel
from scripts.UI.index import UIUpdate
from scripts.background.blackground import BackgroundClass
from scripts.player.index import playerClass




class App(
        playerClass,
        BackgroundClass,
        UIUpdate
    ):
    APP_HEIGHT = 120
    APP_WIDTH = 160

    def __init__(self):
        
        # LOAD ASSETS AND INIT
        pyxel.init(self.APP_WIDTH, self.APP_HEIGHT, caption="Pyxel Jump")
        pyxel.load("assets/sprites.pyxres")

        # PYXEL STARTER
        pyxel.run(self.update, self.draw)

    def draw(self, object = False):

        if object == True:
            pyxel.rect(self.bullet_x, self.bullet_y, self.bullet_w, self.bullet_h, self.BULLET_COLOR)
        else: 
            # DRAWS DEFAULT
            self.drawBackground()
            self.drawUI()
            self.drawPlayer()


    def update(self):
        
        if len(self.bullets_list) > 0:
            self.updateBullet()

        # GAME UPDATES
        self.updatePlayer()
        self.updateBackground()
        self.checkMenuOptions()
        self.updateUI()

App()