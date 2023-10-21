# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
import os
import random
from settings import *
vec = pg.math.Vector2
from random import randint
from sprites import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')





def draw_text(self, text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    self.screen.blit(text_surface, text_rect)


# platforms
 


class Game:
    def __init__(self):
        pg.init
        pg.mixer.init()
        screen = pg.display.set.mode((WIDTH, HEIGHT))
        pg.display.set.caption("My GAME")
        self.clock = pg.time.Clock()
        self.running =  self.clock

    def new(self):
        # create group for all sprites
        all_sprites = pg.sprite.Group()
        all_platforms = pg.sprite.Group()
        all_mobs = pg.sprite.Group()
        self.player = Player(self)
        self.player = Player()
        self.all_platforms.Group

        self.run()

        self.all_sprites.add(plat)



    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
            if player.vel.y > 0:
                hits = pg.sprite.spritecollide(player, all_platforms, False)
            if hits:
                player.pos.y = hits[0].rect.top
                player.vel.y = 0
                
    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                running = False

    def draw(self):
         self.screen.fill(BLACK)
    # draw all sprites
    all_sprites.draw(self.screen)
    draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)

    # buffer - after drawing everything, flip display
    pg.display.flip()





      
# init pygame and create a window


# create a group for all sprites

# instantiate classes
player = Player()


# add instances to groups
all_sprites.add(player)


for p in PLATFORM_LIST:
    # instantiation of the Platform of plat
    plat = Platform(*p)
    all_sprites.add(plat)
    all_platforms.add(plat)

for m in range(0,25):
    m = Mob(randint(0, WIDTH), randint(0,HEIGHT/2), 20, 20, "normal")
    all_sprites.add(m)
    all_mobs.add(m)

# Game loop

# g = Game()
# while g running

    

        
    
    
    ############ Update ##############
    # update all sprites

    # this is what prevents the player from falling through the platform when falling down...
    
    # this prevents the player from jumping up through a platform
    
    
    # if player.vel.y < 0:
    #     hits = pg.sprite.spritecollide(player, all_platforms, False)
    #     if hits:
    #         print("ouch")
    #         SCORE -= 1
    #         if player.rect.bottom >= hits[0].rect.top - 5:
    #             player.rect.top = hits[0].rect.bottom
    #             player.acc.y = 5
    #             player.vel.y = 0


   

pg.quit()


