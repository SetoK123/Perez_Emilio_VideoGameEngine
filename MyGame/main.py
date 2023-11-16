# content from kids can code: http://kidscancode.org/blog/
# Stackoverflow.com - user7343338
# Minh Quan' 25
# Farid Rohana' 25
# Cary Yao' 26


#Goals
# 1. Create Ice mobs - 5/5
# 2. Create coins - 4/5
# 3. create score - 3/5
# 4. Create health - 3/5
# 5. Create more platforms 2/5
# 6. Win Screen 5/5
# 7. Lose Screen 5/5
# 8. Create Background 5/5
# 9. win by coins 5/5
# 10. lose by health





# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
from math import floor

# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')




class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    
    def new(self): 
        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_ice = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_coins = pg.sprite.Group()
        self.all_backs = pg.sprite.Group()
        self.all_floors = pg.sprite.Group()
        self.all_heavans= pg.sprite.Group()
        self.score = 0
        self.health = 5
        
        # Creates Background
        for b in range(0,1):
            b = Back(0,0,WIDTH, HEIGHT)
            self.all_sprites.add(b)
            self.all_backs.add(b)
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)
        self.ground = Platform(*GROUND)
        self.all_sprites.add(self.ground)




# Creates Platforms
        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)
        # create mobs...
        for m in range(0,5):
            m = Mob(randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)

        for i in range(0,5):
            i = Ice(randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 20, 20,)
            self.all_sprites.add(i)
            self.all_ice.add(i)

        for c in range(0,10):
            c = Coin(randint(0, WIDTH), randint(0, math.floor(HEIGHT)), 20, 20,)
            self.all_sprites.add(c)
            self.all_coins.add(c)

# creates floor
        for f in range(0,1):
            f = Floor(0, HEIGHT-40, WIDTH, 40)
            self.all_sprites.add(f)
            self.all_floors.add(f)

# creats the top 
        for h in range(0,1):
            h = Heavan(0, 0, WIDTH, 40)
            self.all_sprites.add(h)
            self.all_heavans.add(h)



        self.run()
# checks for things that happens and updates
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



# If player is jumping check for platform collide
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed*1.5
        
            def update(self):
                self.cd.ticking()

                pg.display.flip()

                
    

        # When the player goes off screen they come back from the other side
        if self.player.pos.x < 0:
            self.player.pos.x = WIDTH
        if self.player.pos.x > WIDTH:
            self.player.pos.x = 0
            
               
            
            

            
                    

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    

    def draw(self):
        ############ Draw ################
        # draw the background screen
        
        

        # #INSIDE OF THE GAME LOOP
        # draw all sprites
        self.all_sprites.draw(self.screen)
        # self.all_sprites.draw(bg)
        self.draw_text("Score: " + str(self.score), 50, WHITE, 500, HEIGHT/10)
        self.draw_text("Health: " + str(self.health), 50, WHITE, 700, HEIGHT/10)
        
        
        
        
    



        
    
        # buffer - after drawing everything, flip display
        pg.display.flip()

        

# Text settings
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

    


g = Game()
while g.running:
    g.new()


pg.quit()