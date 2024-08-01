import pygame
import module.source as source
import module.setClass as setClass

last_time = 0

# 기본키 세팅
def setDefaultPlayerKey():
    global last_time
    
    current_time = pygame.time.get_ticks()
    
    keys = pygame.key.get_pressed()

    player = setClass.player
        
    if keys[pygame.K_LEFT]:
        player.x_pos -= player.speed
        print('←', f'{player.x_pos},{player.y_pos}')
        
    if keys[pygame.K_RIGHT]:
        player.x_pos  += player.speed
        print('→', f'{player.x_pos},{player.y_pos}')
        
    if keys[pygame.K_UP]:
        player.y_pos -= player.speed
        print('↑', f'{player.x_pos},{player.y_pos}')
        
    if keys[pygame.K_DOWN]:
        player.y_pos += player.speed
        print('↓', f'{player.x_pos},{player.y_pos}')
        
    if keys[pygame.K_SPACE]:
        new_bullet = setClass.bullet(player.x_pos, player.y_pos, 10, 10, 200)
        if current_time - last_time > new_bullet.delay:
            setClass.player.bullets.append(new_bullet)
            last_time = current_time
            print('fired')

# 탄 관리

# 총알 업데이트
def update_bullets():
    for bullet in setClass.player.bullets:
        bullet.pos_y -= bullet.speed
        if bullet.pos_y < 0:
            setClass.player.bullets.remove(bullet)