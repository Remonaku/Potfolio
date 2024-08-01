import pygame
import sys
import random
import math
import time

padWidth = 480        # 게임 화면의 가로크기
padHeight = 640       # 게임 화면k의 세로크기

enemyImage = ['pumpkin.png', 'ghost.png', 'franken.png', 'deathgod.png']

explosionSound = ['explosion1.mp3']

crashSound = ['crash.mp3']

wave = pygame.transform.scale(pygame.image.load('wave.png'), (560, 80))
waveSound = ['waveSound.mp3']

fogImage = ['fog.png']
fog02Image = ['fog.png']
fog03Image = ['fog.png']

item_speedImage = ['item_speed.png']
item_bombImage = ['item_bomb.png']
item_heartImage = ['item_heart.png']
item_getImage = ['item_get.png']

# wave 초기 위치 및 속도 설정
waveX = 0
waveY = 0
waveSpeed = 3.5

isWaveActive = False
waveCount = 0 #필살기 갯수 초기화

#목숨 이미지 로드
lifeImage = pygame.image.load('life.png')                                   # 목숨 그림
lifeWidth = 10
lifeHeight = 10

#필살기 타격 카운트 초기화
ultCount = 0
totalCount = 0

#배경화면
background1 = pygame.image.load('NormalBackground.png')
background2 = pygame.image.load('NormalBackground.png')
background3 = pygame.image.load('HardBackground.png')
background4 = pygame.image.load('HardBackground.png')
bgY1 = 0
bgY2 = -padHeight

#스크롤 속도 
scroll_speed = 2  # 배경 스크롤 속도 조절

enemyhitCount = 0  # 맞춘 적의 수 초기화

#파이터 기본 스피드
fighterSpeed = 4


max_wave = 1


############################ 함수 설정 구역 ############################

#난이도
def selectDifficulty():
    global gamePad
    font = pygame.font.Font('neodgm.ttf', 20) 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:  # 노말 모드 선택
                    return '노말'
                elif event.key == pygame.K_h:  # 하드 모드 선택
                    return '하드'
        
        gamePad.fill((70,130,180)) # 화면 색상 : 스틸블루 (70,130,180)

#목숨 그리기
def drawLives(lives):
    global gamePad, lifeImage, lifeWidth, lifeHeight
    
    heartX = 10
    spacing = 35  # 하트 이미지 간격
    for i in range(lives):
        gamePad.blit(lifeImage, ((heartX), 10))
        heartX += lifeWidth + spacing  # 다음 하트를 그리기 위해 x 좌표를 갱신

# 스코어 보드 설정
def writeScore(count):
    global gamePad
    
    font = pygame.font.Font('neodgm.ttf', 20)                              # 폰트는 나눔고딕 20px
    text = font.render('Score : ' + str(count), True, (255,255,255))    # 스코어보드에 출력할 텍스트
    gamePad.blit(text,(360,10))                                                   # 스코어 보드 생성 좌표 (x = 10px, y = 0px)

# 필살기 사용 횟수 표시 설정    
def UltNum(waveCount):
    global gamePad
    font = pygame.font.Font('neodgm.ttf', 20)
    text = font.render('BOMB : ' + str(waveCount), True, (100,100,255))    # 스코어보드에 출력할 텍스트
    gamePad.blit(text,(360,40))
        
# 메세지 출력
def writeMessage(text):
    global gamePad, gameOverSound
    textfont = pygame.font.Font('neodgm.ttf', 30)                  # 폰트는 나눔고딕 80px
    text = textfont.render(text, True, (255,0,0))                       # 게임 오버 시 나오는 텍스트 출력. 색은 빨강(rgb(255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)                                         # text와 textpos 변수 화면에 출력
    pygame.display.update()                                             # 그 후에 화면을 한번 업데이트 한다.
    pygame.mixer.music.stop()                                           # 배경음악 정지                            
    gameOverSound.play()                                                # 게임오버 사운드 재생
    time.sleep(2)                                                       # 2초 대기
    pygame.mixer.music.play(-1)                                         # 배경 음악 재생
    pygame.mixer.music.set_volume(0.4)
    runGame()                                                           # 게임 실행
    
#시작화면
def startMessage(text):
    global gamePad
    textfont = pygame.font.Font('neodgm.ttf', 35)                  # 폰트는 35px
    text = textfont.render(text, True, (255,255,255))                     # 게임 오버 시 나오는 텍스트 출력. 색은 흰색
    textpos = text.get_rect()
    textpos.center = (padWidth/2, 500)
    gamePad.blit(text, textpos)                                         # text와 textpos 변수 화면에 출력
    pygame.display.update()                                             # 그 후에 화면을 한번 업데이트 한다.
    pygame.mixer.music.stop()                                           # 배경음악 정지                            

#정지화면
def gamepaused(text):
    global gamePad
    textfont = pygame.font.Font('neodgm.ttf', 15)
    text = textfont.render(text, True, (255,255,255))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, 400)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()

# 게임 오버 메세지
def gameOver():
    global gamePad, num_lives
    drawLives(num_lives)
    writeMessage('Game Over')                                          # writeMessage 함수에 "게임 오버" 출력
      
# 오브젝트 그리기 
def drawObject(obj, x , y):
    global gamePad
    gamePad.blit(obj, (x, y))
 
# 게임 초기화 함수
def initGame():
    global max_wave, item_getImage, fighterSpeed, ultCount, waveCount, gamePad, clock, background1, background2, fighter, missile, explosion, missileSound, gameOverSound, num_lives, waveSound, crashSound, guideScreen, main
    
    pygame.init()
    
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    
    pygame.display.set_caption('PyShooting')                                    # 게임 이름
    
    background1 = pygame.image.load('NormalBackground.png')                       # 배경 그림
    background2 = pygame.image.load('NormalBackground.png')                       # 배경 그림
    
    main = pygame.image.load('main.png')
    
    guideScreen = pygame.image.load('key_guide_screen.png')                     #키 가이드 화면
    
    fighter = pygame.image.load('fighter.png')                                  # 전투기 그림
    
    missile = pygame.image.load('missile.png')                                  # 미사일 그림
    
    explosion = pygame.image.load('explosion.png')                              # 폭발 그림
    
    pygame.mixer.music.load('background1.mp3')                                        # 배경음악
    
    pygame.mixer.music.play(-1)                                                 # 배경음악 재생
    pygame.mixer.music.set_volume(0.2)
    
    missileSound = pygame.mixer.Sound('attack1.mp3')                            # 미사일 사운드
    
    waveSound = pygame.mixer.Sound('waveSound.mp3')                             #필살기 사운드
        
    gameOverSound = pygame.mixer.Sound('gameover.mp3')                          # 게임오버 사운드
    
    crashSound = pygame.mixer.Sound('crash.mp3')                                # 충돌 사운드
    
    clock = pygame.time.Clock()                                                 # 시간
    
    #필살기 사용횟수, 처치 수 초기화
    ultCount = 0
    
    waveCount = 0

    max_wave = 1

    fighterSpeed = 4

    item_getImage = pygame.image.load('item_get.png')

def runGame():
    
    ##########
    
    gamePaused = True
    
    isDifficulty = True
    
    global fighterSpeed, gamePad, clock, fighter, missile, explosion, missileSound, waveCount, num_lives, difficulty, paused_screen
    
    initGame()
    
    #일시정지 화면 저장
    paused_screen = None 
    
    ###타격 횟수#######
    normalEnemyCount = 0  # 노말 난이도에서는 1대 맞춰야 함
    hardEnemyCount = 0    # 하드 난이도에서는 3대 맞춰야 함
        
    
    # 전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]
    
    # 전투기 초기 위치(x,y) 및 실시간 좌표
    fighterX = padWidth * 0.5 + fighterWidth * 0.5
    fighterY = padHeight * 0.9 - fighterHeight * 0.5
    fighterXspeed = 0
    fighterYspeed = 0
    
    
    # 미사일
    missileXY = []
    
    # 운석 랜덤 생성
    enemy = pygame.image.load(random.choice(enemyImage))
    enemySize = enemy.get_rect().size                                                         # 적 크기
    enemyWidth = enemySize[0]
    enemyHeight = enemySize[1]
    
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))


    # 아이템 크기 설정
    item_speed = pygame.image.load(random.choice(item_speedImage))
    item_speedSize = item_speed.get_rect().size                                                        
    item_speedWidth = item_speedSize[0]
    item_speedHeight = item_speedSize[1]

    item_bomb = pygame.image.load(random.choice(item_bombImage))
    item_bombSize = item_bomb.get_rect().size                                                        
    item_bombWidth = item_bombSize[0]
    item_bombHeight = item_bombSize[1]

    item_heart = pygame.image.load(random.choice(item_heartImage))
    item_heartSize = item_heart.get_rect().size                                                        
    item_heartWidth = item_heartSize[0]
    item_heartHeight = item_heartSize[1]

    # 안개 랜덤 생성
    fog = pygame.image.load(random.choice(fogImage))
    fogSize = fog.get_rect().size                                                        
    fogWidth = fogSize[0]
    fogHeight = fogSize[1]
    
    # 안개 랜덤 생성
    fog02 = pygame.image.load(random.choice(fog02Image))
    fog02Size = fog02.get_rect().size                                                        
    fog02Width = fog02Size[0]
    fog02Height02 = fog02Size[1]
    
    # 안개 랜덤 생성
    fog03 = pygame.image.load(random.choice(fog03Image))
    fog03Size = fog03.get_rect().size                                                        
    fog03Width = fog03Size[0]
    fog03Height = fog03Size[1]
    
    # 운석 초기 위치 설정
    enemyX = random.randrange(0, padWidth - enemyWidth)
    enemyY = 0
    enemySpeed = 4


    # 아이템 초기 위치(숨김)
    item_speedX = random.randrange(0, padWidth - item_speedWidth) #스피드 아이템
    item_speedY = -100
    item_speedSpeed = 0

    item_bombX = random.randrange(0, padWidth - item_bombWidth) #필살기 아이템
    item_bombY = -100
    item_bombSpeed = 0

    item_heartX = random.randrange(0, padWidth - item_heartWidth) #목숨 아이템
    item_heartY = -100
    item_heartSpeed = 0

    # 안개 초기 위치 설정
    fogX = random.randrange(0, padWidth - (fogWidth+80))
    fogY = 0
    fogSpeed = 4
    
    # 안개 초기 위치 설정
    fog02X = random.randrange(0, padWidth - (fog02Width-40))
    fog02Y = -30
    fog02Speed = 3
    
    # 안개 초기 위치 설정
    fog03X = random.randrange(0, padWidth - (fog03Width+50))
    fog03Y = -50
    fog03Speed = 4
    
    # 미사일 운석 타격 여부
    isHit = False
    hitCount = 0
    enemyPassed = 0

    
    
    
    # 게임 실행 True
    onGame = True
    
    # 게임 실행 중
    while onGame:
        
        global max_wave, waveX, waveY, waveSpeed, isWaveActive, ultCount, totalCount, start_pressed, bgY1, bgY2, scroll_speed, enemyhitCount, background1, background2
        
        # 배경 이미지를 스크롤하면서 연결
        bgY1 += scroll_speed
        bgY2 += scroll_speed
        
        if bgY1 >= padHeight:
            bgY1 = -padHeight
        if bgY2 >= padHeight:
            bgY2 = -padHeight

        # 배경 이미지 그리기
        gamePad.blit(background1, (0, bgY1))
        gamePad.blit(background2, (0, bgY2))
        ##########
        if gamePaused:
         
            #startMessage("S키를 눌러 게임시작")

            drawObject(main,0,0)
            pygame.display.update()
            
            start_pressed = False
            
            if paused_screen is None:
                paused_screen = gamePad.copy()
            gamePad.blit(paused_screen, (0, 0))  # 캡쳐된 화면을 그리기
            
            while not start_pressed:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # 게임 프로그램 종료
                        pygame.quit()
                        sys.exit()
                    
                    if event.type in [pygame.KEYDOWN]:
                        drawObject(guideScreen,0,0)
                        pygame.display.update()
                        if event.key == pygame.K_s:
                            start_pressed = True
                            gamePaused = False  # S 키를 누르면 게임 시작
                            pygame.mixer.music.play(-1)                                         # 배경 음악 재생
                            pygame.mixer.music.set_volume(0.2)
                            continue  # 게임 시작 후 게임 루프를 진행하도록 continue 사용

            
            if isDifficulty :   # 초기에는 난이도선택여부 True 라서 선택가능. 게임 진행 후에는 False로 변경
                #난이도 선택 화면 표시
                difficulty = selectDifficulty()
                
                # 난이도에 따라 목숨 설정
                if difficulty == '노말':
                    num_lives = 5
                    normalEnemyCount = 1
                    
                    
                    
                elif difficulty == '하드':
                    num_lives = 3
                    hardEnemyCount = 3
                    background1 = background3
                    background2 = background4
            


            
        
        #########                        
        if not gamePaused :
            isDifficulty = False    # 난이도선택여부 게임 진행 후에는 False로 변경.
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 게임 프로그램 종료
                    pygame.quit()
                    sys.exit()


                    
                if event.type in [pygame.KEYDOWN]:
                    
                    if event.key == pygame.K_LEFT:                                                  # 전투기 왼쪽으로
                        if fighterXspeed > 0:
                            fighterXspeed -= 2 * fighterSpeed
                        else: fighterXspeed -= fighterSpeed
                        
                    elif event.key == pygame.K_RIGHT:                                               # 전투기 오른쪽으로
                        if fighterXspeed < 0:
                            fighterXspeed += 2 * fighterSpeed
                        else: fighterXspeed += fighterSpeed
                        
                    elif event.key == pygame.K_UP:                                                  # 전투기 위쪽으로
                        if fighterYspeed > 0:
                            fighterYspeed -= 2 * fighterSpeed
                        else: fighterYspeed -= fighterSpeed
                        
                    elif event.key == pygame.K_DOWN:                                                # 전투기 아랫쪽으로
                        if fighterYspeed < 0:
                            fighterYspeed += 2 * fighterSpeed
                        else: fighterYspeed += fighterSpeed
                        
                    elif event.key == pygame.K_SPACE:                                               # 미사일 발사
                        missileSound.play()                                                         # 미사일 사운드 재생
                        missileSound.set_volume(0.2)
                        missileX = fighterX + fighterWidth/2
                        missileY = fighterY - fighterHeight + 100
                        missileXY.append([missileX, missileY])
                        
                    elif event.key == pygame.K_f and not isWaveActive:  # f 키를 눌렀을 때 wave 생성
                        waveY = fighterY  # wave의 y 좌표를 fighter의 y 좌표와 같게 설정
                        if waveCount > 0:
                            isWaveActive = True  # wave가 활성화됨
                            waveCount -= 1
                            
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            if gamePaused:
                                gamePaused = False  # 일시정지 해제
                            else:
                                gamePaused = True
                                gamepaused("S키를 눌러 게임 재개")
  

                    
                if event.type in [pygame.KEYUP]:                                                    # 방향키를 떼면 전투기 멈춤
                    if event.key == pygame.K_LEFT:
                        if fighterXspeed < 0:
                            fighterXspeed = 0
                            
                    if event.key == pygame.K_RIGHT:
                        if fighterXspeed > 0:
                            fighterXspeed = 0
                            
                    if event.key == pygame.K_UP:
                        if fighterYspeed < 0:
                            fighterYspeed = 0
                        
                    if event.key == pygame.K_DOWN:
                        if fighterYspeed > 0:
                           fighterYspeed = 0
                                                   
        drawLives(num_lives)
        
        # wave 이동
        waveY -= waveSpeed
        
        # wave가 화면 위로 벗어나면 초기화
        if waveY < 40:
            waveX = 0
            waveY = fighterY
            isWaveActive = False   # wave를 초기화하면 비활성화
            
        # wave 이미지를 그리기
        if isWaveActive:
            if waveY <= enemyY:
                
                drawObject(explosion, enemyX, enemyY)                                                 # 적 폭발 이펙트
                waveSound.play()                                                                 # 필살기 사운드 재생
                waveSound.set_volume(0.7)

                # 새로운 운석(랜덤)
                enemy = pygame.image.load(random.choice(enemyImage))
                enemySize = enemy.get_rect().size                                                     
                enemyWidth = enemySize[0]
                enemyHeight = enemySize[1]
                enemyX = random.randrange(0, padWidth - enemyWidth)
                enemyY = 0
                destroySound = pygame.mixer.Sound(random.choice(explosionSound))
                isHit = False
                enemyhitCount = 0    
                ultCount += 10
            drawObject(wave, waveX-20, waveY)
        
        
        # 전투기 실시간 좌표 변경
        fighterX += fighterXspeed
        fighterY += fighterYspeed
        
        # 운석 실시간 좌표
        enemyY += enemySpeed                       # 운석 아래로 움직임

        # 아이템 실시간 좌표(일단 정지상태)
        item_speedY += item_speedSpeed
        item_bombY += item_bombSpeed
        item_heartY += item_heartSpeed

        # 안개 실시간 좌표
        fogY += fogSpeed                       # 운석 아래로 움직임
        fog02Y += fog02Speed
        fog03Y += fog03Speed
        
        # 경계선 결정        
        if fighterX < 0:
            fighterX = 0
            
        elif fighterX > padWidth - (fighterWidth):
            fighterX = padWidth - (fighterWidth)
            
        if fighterY < 0:
            fighterY = 0
            
        elif fighterY > padHeight - (fighterHeight):
            fighterY = padHeight - (fighterHeight)
        
        
            
        # 충돌 판정 박스
        mX = 1                                                                                  # 배율(히트박스 크기 조절)
        mY = 0.3
        


        # fighter의 실시간 x좌표와 y좌표 사이에 enemy 중심좌표가 있다면 crash() 판정
        if fighterX - fighterWidth * mX < enemyX < fighterX + fighterWidth * mX \
            and fighterY - fighterHeight * mY < enemyY < fighterY + fighterHeight * mY:     
                
                drawObject(explosion, enemyX, enemyY)                                                 # 적 폭발 이펙트
                crashSound.play()                                                                 # 적 폭발 사운드 재생
                crashSound.set_volume(0.4)

                
                # 새로운 운석(랜덤)
                enemy = pygame.image.load(random.choice(enemyImage))
                enemySize = enemy.get_rect().size                                                     # 적 크기
                enemyWidth = enemySize[0]
                enemyHeight = enemySize[1]
                enemyX = random.randrange(0, padWidth - enemyWidth)
                enemyY = 0
                destroySound = pygame.mixer.Sound(random.choice(explosionSound))  
                num_lives -= 1
                if num_lives == 0:
                    gameOver()
                else:
                    drawLives(num_lives)        #목숨 그림 감소
                                                                                    
                 
        drawObject(fighter, fighterX, fighterY)                                                 # 비행기를 게임 화면의(x,y) 좌표에 그림
        
        # 일정 점수 얻을 때마다 고정됐던 아이템이 속도를 갖고 내려옴
        if totalCount != 0 and totalCount % 80 == 0:
            item_speedSpeed = 2
                    
        if totalCount != 0 and totalCount % 130 == 0:
            item_bombSpeed = 2

        if totalCount != 0 and totalCount % 170 == 0:
            item_heartSpeed = 2

        
            
        # 아이템과 부딪히면
        if fighterX - fighterWidth * mX < item_speedX < fighterX + fighterWidth * mX \
            and fighterY - fighterHeight * mY < item_speedY < fighterY + fighterHeight * mY:     
                
                fighterSpeed += 1.5
                if fighterSpeed > 8.5:
                    fighterSpeed = 8.5

                drawObject(item_getImage, item_speedX, item_speedY)

                item_speed = pygame.image.load(random.choice(item_speedImage))
                item_speedSize = item_speed.get_rect().size
                item_speedWidth = item_speedSize[0]
                item_speedHeight = item_speedSize[1]
                item_speedX = random.randrange(0, padWidth - item_speedWidth)
                item_speedY = -100
                item_speedSpeed = 0
                                                                                                    
        if fighterX - fighterWidth * mX < item_bombX < fighterX + fighterWidth * mX \
            and fighterY - fighterHeight * mY < item_bombY < fighterY + fighterHeight * mY:     
                        
                max_wave += 1
                waveCount += 1

                drawObject(item_getImage, item_bombX, item_bombY)

                item_bomb = pygame.image.load(random.choice(item_bombImage))
                item_bombSize = item_bomb.get_rect().size
                item_bombWidth = item_bombSize[0]
                item_bombHeight = item_bombSize[1]
                item_bombX = random.randrange(0, padWidth - item_bombWidth)
                item_bombY = -100
                item_bombSpeed = 0

        if fighterX - fighterWidth * mX < item_heartX < fighterX + fighterWidth * mX \
            and fighterY - fighterHeight * mY < item_heartY < fighterY + fighterHeight * mY:     
                
                if difficulty == '노말' and num_lives < 5:
                        num_lives += 1

                elif difficulty == '하드' and num_lives < 3:
                        num_lives += 1

                drawObject(item_getImage, item_heartX, item_heartY)

                item_heart = pygame.image.load(random.choice(item_heartImage))
                item_heartSize = item_heart.get_rect().size
                item_heartWidth = item_heartSize[0]
                item_heartHeight = item_heartSize[1]
                item_heartX = random.randrange(0, padWidth - item_heartWidth)
                item_heartY = -100
                item_heartSpeed = 0


        # 미사일 발사
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):                                                 # 미사일 요소에 대해 반복
                bxy[1] -= 10                                                                    # 총알의 y좌표 -10(위로 이동)
                missileXY[i][1] = bxy[1]
                
                # 미사일이 운석을 맞추었을 경우
                if bxy[1] < enemyY:
                    if bxy[0] > enemyX-15 and bxy[0] < enemyX + enemyWidth:
                        missileXY.remove(bxy)
                        enemyY -= 15
                        isHit = True
                        enemyhitCount += 1
                        
                    

                        
                # 미사일이 화면 밖을 벗어나면
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)                                                   # 미사일 제거
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)
        
        
        totalCount = hitCount + ultCount
        writeScore(totalCount)                                                                    # 운석 맞춘 점수 표시
        
        # 필살기 사용횟수 표시
        UltNum(waveCount)                                                                    # 운석 맞춘 점수 표시
        
        #안개 통과
        if fogY > padHeight:
            #새로운 안개 생성
            fog = pygame.image.load(random.choice(fogImage))
            fogSize = fog.get_rect().size                                                     
            fogWidth = fogSize[0]
            fogHeight = fogSize[1]
            fogX = random.randrange(0, padWidth - fogWidth)
            fogY = 0
            drawObject(fog, fogX, fogY)
            
        if fog02Y > padHeight:
            #새로운 안개 생성
            fog02 = pygame.image.load(random.choice(fog02Image))
            fog02Size = fog02.get_rect().size                                                     
            fog02Width = fog02Size[0]
            fog02Height = fog02Size[1]
            fog02X = random.randrange(0, padWidth - fog02Width)
            fog02Y = 0
            drawObject(fog02, fog02X, fog02Y)
            
        if fog03Y > padHeight:
            #새로운 안개 생성
            fog03 = pygame.image.load(random.choice(fog03Image))
            fog03Size = fog03.get_rect().size                                                     
            fog03Width = fog03Size[0]
            fog03Height = fog03Size[1]
            fog03X = random.randrange(0, padWidth - fog03Width)
            fog03Y = 0
            drawObject(fog03, fog03X, fog03Y)


        # 아이템 통과시
        if item_speedY > padHeight:
            item_speed = pygame.image.load(random.choice(item_speedImage))
            item_speedSize = item_speed.get_rect().size
            item_speedWidth = item_speedSize[0]
            item_speedHeight = item_speedSize[1]
            item_speedX = random.randrange(0, padWidth - item_speedWidth)
            item_speedY = -100
            item_speedSpeed = 0

        if item_bombY > padHeight:
            item_bomb = pygame.image.load(random.choice(item_bombImage))
            item_bombSize = item_bomb.get_rect().size
            item_bombWidth = item_bombSize[0]
            item_bombHeight = item_bombSize[1]
            item_bombX = random.randrange(0, padWidth - item_bombWidth)
            item_bombY = -100
            item_bombSpeed = 0

        if item_heartY > padHeight:
            item_heart = pygame.image.load(random.choice(item_heartImage))
            item_heartSize = item_heart.get_rect().size
            item_heartWidth = item_heartSize[0]
            item_heartHeight = item_heartSize[1]
            item_heartX = random.randrange(0, padWidth - item_heartWidth)
            item_heartY = -100
            item_heartSpeed = 0

        # 운석을 통과시킨 경우
        if enemyY > padHeight:
            # 새로운 운석(랜덤)
            enemy = pygame.image.load(random.choice(enemyImage))
            enemySize = enemy.get_rect().size                                                     # 운석 크기
            enemyWidth = enemySize[0]
            enemyHeight = enemySize[1]
            enemyX = random.randrange(0, padWidth - enemyWidth)
            enemyY = 0
            #놓친 갯수 만큼 목숨 감소      
            num_lives -= 1
            if num_lives == 0:
                gameOver()
            else:
                drawLives(num_lives)        #목숨 그림 감소

        
        # 운석을 맞춘 경우
        if isHit:        
            if difficulty == '노말':
                if enemyhitCount >= normalEnemyCount:
                        # 운석 폭발
                    drawObject(explosion, enemyX, enemyY)                                                 # 운석 폭발 이펙트
                    destroySound.play()                                                                 # 운석 폭발 사운드 재생
                    destroySound.set_volume(0.4)
                    
                    
                    # 새로운 운석(랜덤)
                    enemy = pygame.image.load(random.choice(enemyImage))
                    enemySize = enemy.get_rect().size                                                     # 운석 크기
                    enemyWidth = enemySize[0]
                    enemyHeight = enemySize[1]
                    enemyX = random.randrange(0, padWidth - enemyWidth)
                    enemyY = 0
                    destroySound = pygame.mixer.Sound(random.choice(explosionSound))
                    isHit = False
                    enemyhitCount = 0
                    
                    
                    hitCount += 10 # 점수 계산
                    if waveCount < max_wave:
                        if hitCount % 100 == 0:
                            waveCount += 1
                            if waveCount > max_wave:
                                waveCount = max_wave

                        # 운석 맞추면 속도 증가 (난이도)
                        enemySpeed += 0.02
                        if enemySpeed >= 20:
                            enemySpeed = 20
                    


            if difficulty == '하드':    
                if enemyhitCount >= hardEnemyCount:
                        # 운석 폭발
                    drawObject(explosion, enemyX, enemyY)                                                 # 운석 폭발 이펙트
                    destroySound.play()                                                                 # 운석 폭발 사운드 재생
                    destroySound.set_volume(0.4)
                                        
                    # 새로운 운석(랜덤)
                    enemy = pygame.image.load(random.choice(enemyImage))
                    enemySize = enemy.get_rect().size                                                     # 운석 크기
                    enemyWidth = enemySize[0]
                    enemyHeight = enemySize[1]
                    enemyX = random.randrange(0, padWidth - enemyWidth)
                    enemyY = 0
                    destroySound = pygame.mixer.Sound(random.choice(explosionSound))
                    isHit = False
                    enemyhitCount = 0               
                    

                    # 운석 맞추면 속도 증가 (난이도)
                    enemySpeed += 0.02
                    if enemySpeed >= 20:
                        enemySpeed = 20
                        
                    hitCount += 10 # 10개 맞췄을 경우 필살기 1개 추가
                    if hitCount % 100 == 0:
                            waveCount = 1

            
           
        drawObject(item_speed, item_speedX, item_speedY)
        drawObject(item_bomb, item_bombX, item_bombY)        
        drawObject(item_heart, item_heartX, item_heartY)  
        drawObject(fog, fogX, fogY)       
        drawObject(fog02, fog02X, fog02Y)        
        drawObject(fog03, fog03X, fog03Y)        
        drawObject(enemy, enemyX, enemyY)                  # 운석 그리기
        pygame.display.update()                         # 게임화면을 다시 그림
        clock.tick(60)                                  # 게임화면의 초당 프레임수를 60으로 설정
        

        
    pygame.quit()   #pygame 종료



# 게임 초기화    
initGame()

# 게임 실행
runGame()
