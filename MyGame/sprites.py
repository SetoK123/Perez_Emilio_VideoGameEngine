import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *
import time 
from math import floor

import random

from random import randint
    
# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')


# creates class for background

class Back(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.image = pg.image.load(os.path.join(img_folder, 'Background.png')).convert()



# creates player 
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # self.image = pg.Surface((50, 50))
        # self.image.fill(GREEN)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.game.score = 0

        self.game.health = 5
        # controls for player
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
        
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        ghits = pg.sprite.collide_rect(self, self.game.ground)
        if hits or ghits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        # CHECKING FOR COLLISION WITH MOBS HERE>>>>>
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos


    
# checks for mob hit and -1 health then checks for health if = 0 they shows lose screen
        mhits = pg.sprite.spritecollide(self, self.game.all_mobs, True)
        if mhits:
            mhits[0].tagged = True
            # self.game.score -= 1
            self.game.health -= 1
            if self.game.health == 0:
                self.game.screen.blit(pg.image.load(os.path.join(img_folder, "GameOver.png")).convert(), (0,0))
                pg.display.flip()
                time.sleep(2) 
                pg.quit()
            

            
            
            
            

            # checks for ice mob hit and -1 health then checks for health if = 0 they shows lose screen
        ihits = pg.sprite.spritecollide(self, self.game.all_ice, True)
        if ihits:
            ihits[0].tagged = True
            time.sleep(3)
            # self.game.score -= 1
            self.game.health -= 1
            if self.game.health == 0:
                self.game.screen.blit(pg.image.load(os.path.join(img_folder, "GameOver.png")).convert(), (0,0))
                pg.display.flip()
                time.sleep(2) 
                pg.quit()
            
           
            
            


# checks for coin collect then increases score +1 and when score reaches 5 win screen shows
        chits = pg.sprite.spritecollide(self, self.game.all_coins, True)
        if chits:
            self.game.score += 1
            if self.game.score == 5:
                self.game.screen.blit(pg.image.load(os.path.join(img_folder, "Win.png")).convert(), (0,0))
                pg.display.flip()
                time.sleep(2) 
                pg.quit()
            

        

        # When player hits ground they get a game over and game closes
        fhits = pg.sprite.spritecollide(self, self.game.all_floors, False)
        if fhits:
            
            self.game.screen.blit(pg.image.load(os.path.join(img_folder, "GameOver.png")).convert(), (0,0))
            pg.display.flip()
            time.sleep(2) 
            pg.quit()

# When player reaches top they get a win screen
        hhits = pg.sprite.spritecollide(self, self.game.all_heavans, False)
        if hhits:
            
            self.game.screen.blit(pg.image.load(os.path.join(img_folder, "Win.png")).convert(), (0,0))
            pg.display.flip()
            time.sleep(2) 
            pg.quit()

        

            
            

   
            
            
            
            
            
            
            


       


# platforms

class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.image = pg.image.load(os.path.join(img_folder, 'Wood.png')).convert()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed

# Creates mob
class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.image = pg.image.load(os.path.join(img_folder, 'Mob.png')).convert()

# Creates Ice mob
class Ice(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.image = pg.image.load(os.path.join(img_folder, 'Ice.png')).convert()
        
# Creates coin
class Coin(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.image = pg.image.load(os.path.join(img_folder, 'coin.png.png')).convert()
        self.image.set_colorkey(BLACK)
        
# Creates the floor
class Floor(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pg.image.load(os.path.join(img_folder, 'floor.png')).convert()

# creates the top
class Heavan(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pg.image.load(os.path.join(img_folder, 'heavan.png')).convert()
        self.image.set_colorkey(BLACK)
        

    

        
        

    

    def update(self):
        pass