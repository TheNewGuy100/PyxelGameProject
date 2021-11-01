
from scripts.UI.healthBar import healthBarStatus
from scripts.UI.options import optionsClass
from scripts.UI.score import scoreClass


class UIUpdate(
    optionsClass,
    scoreClass,
    healthBarStatus
):
    def drawUI(self):
        self.drawScore()
        self.drawHealthBar()

    def updateUI(self):
        self.checkMenuOptions()
        self.drawScore()
        self.checkHealth()

