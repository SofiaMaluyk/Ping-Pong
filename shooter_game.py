from pygame import * 
from random import *
from time import time as timer  
window = display.set_mode((700,500))
display.set_caption('Шутер')
galaxy = transform.scale(image.load('galaxy.jpg'), (700, 500))
x1 = 65
y1 = 65

clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def resent(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y  < 400:
            self.rect.y += self.speed

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y  < 400:
            self.rect.y += self.speed

sprite1 = Player('platform.png', 70, 100, 5, 20, 250)
sprite2 = Player('platform.png', 600, 100, 5, 20, 250)


run = True
while run:
    window.blit(galaxy,(0,0))

    for e in event.get():
        if e.type == QUIT:
            run = False
        

       

            

    sprite1.resent()
    sprite1.update()

    sprite2.resent()
    sprite2.update()
        


    display.update()
    clock.tick(FPS)






