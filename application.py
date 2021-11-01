
import pyxel
from scripts.UI.index import UIUpdate
from scripts.UI.options import optionsClass
from scripts.UI.score import scoreClass
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
        pyxel.load("assets/jump_game.pyxres")

        # PYXEL STARTER
        pyxel.run(self.update, self.draw)

    def draw(self):
        
        pyxel.cls(12)

        # DRAWS
        self.drawBackground()
        self.drawUI()

    def update(self):

        # GAME UPDATES
        self.updatePlayer()
        self.updateBackground()
        self.checkMenuOptions()
        self.updateUI()

App()