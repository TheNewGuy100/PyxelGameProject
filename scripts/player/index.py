
from scripts.player.checkPlayerDead_sub import playerCheckDead
from scripts.player.drawPlayer_sub import drawPlayerInit
from scripts.player.playerAnimations_sub import playerAnimations
from scripts.player.playerMovement_sub import playerMovement


class playerClass(
    drawPlayerInit,
    playerMovement,
    playerCheckDead,
    playerAnimations
):
    player_x = 6
    player_y = 53
    player_vy = 0
    player_is_alive = True

    # GAME UPDATES MID-GAME
    def updatePlayer(self):
        self.checkPlayerAnimations()
        self.checkPlayerDead()
        self.checkPlayerMovement()
