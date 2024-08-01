import pygame
import module.source as source

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


class character:
    
    bullets = []
    
    def __init__(self,name,hp,atk,speed):
        self.width = name.get_width()
        self.height = name.get_height()
        self.x_pos = self.width//2
        self.y_pos = self.height//2
        self.hp = hp
        self.atk = atk
        self.speed = speed

class bullet:
    def __init__(self, pos_x, pos_y, speed, damage, delay):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.damage = damage
        self.delay = delay

player = character(source.player,100,10,5)