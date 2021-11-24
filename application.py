
import pyxel
from scripts.UI.headshotFeedBack import headShotPopUp
from scripts.UI.index import UIUpdate
from scripts.background.blackground import BackgroundClass
from scripts.mechanics.ammoFind import ammoSpawner
from scripts.mechanics.enemies import enemyClass
from scripts.mechanics.medkitFind import medkitSpawner
from scripts.player.index import playerClass
from scripts.player.playerShoot import bulletsController

class App(
        playerClass,
        enemyClass,
        BackgroundClass,
        UIUpdate,
        bulletsController,
        ammoSpawner,
        medkitSpawner,
        headShotPopUp
    ):

    APP_HEIGHT = 120
    APP_WIDTH = 160
    
    APP_Y_MIN_PLAYABLE_AREA = 30
    APP_Y_MAX_PLAYABLE_AREA = 100
    APP_X_MIN_PLAYABLE_AREA = 0
    APP_X_MAX_PLAYABLE_AREA = 160
    
    def __init__(self):
        pyxel.init(
            self.APP_WIDTH,
            self.APP_HEIGHT,
            caption="Zombies Invasion 1.0"
        )
        pyxel.load("assets/sprites.pyxres")
        pyxel.run(
            self.update,
            self.draw
        )

    def draw(self):
        self.drawBackground()
        self.drawUI()
        self.drawPlayer()
        self.drawBullets()
        self.drawEnemys()
        self.drawAmmoBox()
        self.drawMedkitBox()
        self.gameOverCheck()
        self.drawHeadShots()

    def update(self):
        self.updatePlayer()
        self.updateBackground()
        self.checkMenuOptions()
        self.updateUI()
        self.updateBullet()
        self.updateEnemys()
        self.spawnAmmoInMap()
        self.spawnMedkitInMap()

# APPLICATION CALL
App()