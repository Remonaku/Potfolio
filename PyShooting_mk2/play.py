import pygame
import sys
import random
import math
import time
import module.source as source
import module.setup as setup
import module.setClass as setClass
import module.object as object

from module.setClass import player


# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 창 제목 설정
pygame.display.set_caption('Pygame 테스트 중....')

# 색상 정의 (RGB 값)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# 프레임 설정
clock = pygame.time.Clock()
fps = 60

# 게임 시간 설정
gametime = pygame.time.get_ticks()

# ===============================================================================================


# 게임 루프
stage_1 = True
stage_2 = False
stage_3 = False

#==================== stage 1 ====================

while stage_1:
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    # 화면을 검은색으로 채우기
    screen.fill((0, 0, 0))
    
    source.animation('슬라임',100, 200, 100)
    
    if pygame.key.get_pressed()[pygame.K_RETURN]:
        print('stage change 1 to 2')
        stage_1 = False
        stage_2 = True

    pygame.display.flip()

time.sleep(0.3)

#==================== stage 2 ====================

while stage_2:
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    # 화면을 빨간색으로 채우기
    screen.fill((255, 0, 0))
    
    if pygame.key.get_pressed()[pygame.K_RETURN]:
        print('stage change 2 to 3')
        stage_2 = False
        stage_3 = True
        
    pygame.display.flip()

time.sleep(0.3)

#==================== stage 3 ====================

while stage_3:
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    setup.setDefaultPlayerKey()
    
    setup.update_bullets()
    
    # 화면을 흰색으로 채우기
    screen.fill((255,255,255))
    
    # 플레이어 화면에 표시
    screen.blit(source.player, (player.x_pos, player.y_pos))
    
    # 총알을 화면에 표시
    for bullet in setClass.player.bullets:
        screen.blit(source.bullet, (bullet.pos_x, bullet.pos_y))
    
    # 화면 업데이트
    pygame.display.flip()

    # 프레임 맞추기
    clock.tick(fps)

# Pygame 종료
pygame.quit()
sys.exit()