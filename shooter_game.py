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
font.init()



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
ball = GameSprite('ball_1615463127.png', 100, 100, 2, 60, 60)

speed_x = 2
speed_y = 2
finish = False

font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    window.blit(galaxy,(0,0))

   
    if finish != True:
       ball.rect.x += speed_x
       ball.rect.y += speed_y

    if ball.rect.y > 450 or ball.rect.y <0:
        speed_y *= -1

    if sprite.collide_rect(sprite1, ball) or sprite.collide_rect(sprite2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 700:
        finish = True
        window.blit(lose1, (200, 200))



    sprite1.resent()
    sprite1.update_l()

    sprite2.resent()
    sprite2.update_r()

    ball.resent()
    ball.update()
    
        

       

            

    
        


    display.update()
    clock.tick(FPS)
