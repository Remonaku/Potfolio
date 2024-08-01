import pygame
import os
import time

pygame.mixer.init()



screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))



def width(name):
    width = name.get_width()
    return width

def height(name):
    height = name.get_height()
    return height

# ====== 소스 저장소 ======


# 플레이어
bullet = pygame.image.load('resource/image/player/missile.png')
player = pygame.image.load('resource/image/player/player.png')

print('Player Image Sources All Loaded!')

# ===========================================================================================

# 적군
death = pygame.image.load('resource/image/enemy/death.png')
franken = pygame.image.load('resource/image/enemy/franken.png')
ghost = pygame.image.load('resource/image/enemy/ghost.png')
pumpkin = pygame.image.load('resource/image/enemy/pumpkin.png')

print('Enemy Image Sources All Loaded!')

# ===========================================================================================

# 아이템
speedUp = pygame.image.load('resource/image/item/item_speed.png')
life = pygame.image.load('resource/image/item/item_life.png')
bomb = pygame.image.load('resource/image/item/item_bomb.png')

print('Item Image Sources All Loaded!')

# ===========================================================================================

# 효과음
# pygame.mixer.init 사용
ef_explosion = pygame.mixer.Sound('resource/sound/explosion1.mp3')
# ef_explosion.set_volume(0.5) // 정수로 조절

print('Effect Sound Sources All Loaded!')

# ===========================================================================================

# 배경음
bgm1 = pygame.mixer.music.load('resource/sound/background1.mp3')
# pygame.mixer.music.play(-1) // 무한재생

print('BGM Sound Sources All Loaded!')

# ===========================================================================================

# 애니메이션 로드 함수
# 경로 = resource/image/animation/example

animation_list = {}

def load_animation(root,animation_name):
    sprite = []
    for file in os.listdir(root):
        sprite.append(f'{root}/{file}')
    
    animation_list[animation_name] = sprite
    

def animation(animation_name, x, y, fps):
    timer = pygame.time.get_ticks()

# ===========================================================================================


load_animation('resource/image/animation/example','슬라임')
print(animation_list)