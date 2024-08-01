import pygame
import sys
import setClass
import time
import os


# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 600
screen_height = 600
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

# ===============================================================================================


# 게임 루프
stage = True

while stage:
    
    last_time = 0
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    screen.fill((255,255,255))
    
    for i in range(1,len(os.listdir('slime'))+1):
        
        run_time = pygame.time.get_ticks()
        slime_img = pygame.image.load(f'slime/Slime_{i}.png')
        
        if run_time - last_time < 1000:
            screen.fill((255,255,255))
            screen.blit(slime_img, (setClass.slime.x_pos, setClass.slime.y_pos))
            print(f'run time: {run_time}, latest time: {last_time}, img: Slime_{i}')
            
        else:
            last_time = run_time
            pygame.display.flip()   # 이거 안붙이면 애니메이션 갱신이 안됨
            continue

            
    # for img in os.listdir('slime'):
        
    #     # 화면을 흰색으로 채우기
    #     screen.fill((255,255,255))
    #     slime_img = pygame.image.load(f'slime/{img}')
    #     screen.blit(slime_img, (setClass.slime.x_pos, setClass.slime.y_pos))
    #     pygame.display.flip()   # 이거 안붙이면 애니메이션 갱신이 안됨
    #     print(f'{img}')
    #     time.sleep(0.2)
    
    # 화면 업데이트
    pygame.display.flip()

    # 프레임 맞추기
    clock.tick(fps)

# Pygame 종료
pygame.quit()
sys.exit()