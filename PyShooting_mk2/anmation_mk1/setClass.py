import pygame

# 화면 설정
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

slime_img = pygame.image.load('slime/Slime_1.png')

class character:
    
    def __init__(self,name):
        self.width = name.get_width()
        self.height = name.get_height()
        self.x_pos = self.width//2
        self.y_pos = self.height//2

slime = character(slime_img)