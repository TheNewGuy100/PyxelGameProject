
import pyxel

from scripts.blackground import BackgroundClass
from scripts.player import playerClass
from scripts.score import scoreClass



class App(
        playerClass,
        BackgroundClass, 
        scoreClass
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
        self.drawScore()
        self.drawPlayer()

    def update(self):
        
        # QUIT GAME
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        # GAME UPDATES
        self.updatePlayer()
        self.updateBackground()

App()