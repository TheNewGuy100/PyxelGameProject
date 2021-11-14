
import random
import pyxel

class enemyClass():
    frame_start = 100
    enemys_list = []
    enemys_limit = 10
    enemy_position_x = 0
    enemy_position_y = 0
    enemy_sprite_u1 = 64
    enemy_sprite_v1 = 0
    enemy_sprite_u2 = 80
    enemy_sprite_v2 = 0
    enemy_speed_max = 6
    enemy_speed_min = 1
    enemy_spawn_range_min = 30
    enemy_spawn_range_max = 60
    enemy_delay = 0
    color_key = 12

    def drawEnemys(self):
        if  (pyxel.frame_count > self.frame_start):
            if (self.enemys_list.__len__() > 0):
                for enemy in self.enemys_list:
                    if enemy != None:
                        if enemy['u'] == self.enemy_sprite_u1 and pyxel.frame_count % 20 == 1:
                            enemy['u'] = self.enemy_sprite_u2
                        else:
                            enemy['u'] = self.enemy_sprite_u1
                        pyxel.blt(
                            enemy['x'],
                            enemy['y'],
                            enemy['img'],
                            enemy['u'],
                            enemy['v'],
                            enemy['w'],
                            enemy['h'],
                            enemy['colkey']
                        )

    def updateEnemys(self):
        if (pyxel.frame_count > self.frame_start):
            if ( pyxel.frame_count >= self.enemy_delay and self.enemys_list.__len__() < self.enemys_limit):
                self.enemy_delay = pyxel.frame_count + 30
                
                self.enemys_list.append({
                    "x": self.APP_X_MAX_PLAYABLE_AREA + random.randint(self.enemy_spawn_range_min, self.enemy_spawn_range_max),
                    "y": random.randint(self.APP_Y_MIN_PLAYABLE_AREA, self.APP_Y_MAX_PLAYABLE_AREA),
                    "img": 0,
                    "u": self.enemy_sprite_u1,
                    "v": self.enemy_sprite_v1,
                    "w": 16,
                    "h": 16,
                    "colkey": self.color_key,
                })
        
        if  (pyxel.frame_count > self.frame_start):
            if (self.enemys_list.__len__() > 0):
                for index_enemy, enemy in enumerate(self.enemys_list):
                    if enemy != None:
                        enemy['x'] -= random.randint(self.enemy_speed_min, self.enemy_speed_max)
                    if (enemy['x'] < self.APP_X_MIN_PLAYABLE_AREA):
                        self.enemys_list.pop(index_enemy)