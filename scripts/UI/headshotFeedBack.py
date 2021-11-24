
import pyxel

class headShotPopUp():
    headShotsList = []
    framesLimit = 30
    headShotObject = {
        "x": 0,
        "y": 0,
        "type": 0,
        "0": 7,
        "1": 10,
        "message": "HEADSHOT!",
        "framesLimit": 0
    }

    def AddHeadShot(self, x, y):
        self.headShotObject['x'] = x
        self.headShotObject['y'] = y
        self.headShotObject['framesLimit'] = pyxel.frame_count + self.framesLimit
        self.headShotsList.append(self.headShotObject)

    def drawHeadShots(self):
        for index, headShotMessage in enumerate(self.headShotsList):
            if (headShotMessage['framesLimit'] >= pyxel.frame_count ):
                pyxel.text(
                    headShotMessage['x'],
                    headShotMessage['y'],
                    headShotMessage['message'],
                    headShotMessage['type']
                )

                if pyxel.frame_count % 5 == 1:
                    if headShotMessage['type'] == 1:
                        headShotMessage['type'] = 0
                    else:
                        headShotMessage['type'] = 1
            else:
                self.headShotsList.pop(index)