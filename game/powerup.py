#Place power up sprite in random bricks
#Fall at 3 pixels per frame
#duplicate all balls by 2
#triggered with contact on paddle



import pygame
from random import randrange
from game.constants import Constants
from game.ball import Ball
from game.bricks import Bricks


class Powerup(pygame.sprite.Sprite): #created powerup class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/element_blue_diamond_glossy.png').convert_alpha()
        

        for Bricks in range(Constants.brick_cols, Constants.brick_cols):
            if randrange(5) == 3:
                self.image = pygame.image.load('assets/element_blue_diamond_glossy.png').convert_alpha()


    def fall_down(self): #falling funciton
        self.y_pos = powerup_speed

    def check_collide_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            Ball(self) * 2 #this does not work I bet... YEP!
            powerup.kill() #might kill all powerups still in bricks

    def is_off_screen(self): #kill powerup if falls off screen
        powerup.kill()



