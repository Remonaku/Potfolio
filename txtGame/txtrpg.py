import time
import random as rn

# 확률 계산
# 확률 = num%

def percent(num):

    pullout_num = []

    # 원하는 확률값
    for i in range(1, num+1):
        pullout_num.append(i)
    #print(f'확률 = {num}%')

    # 뽑을 값(중복없이)
    pick = rn.randrange(1,101)

    #print(f'확률 = {set(pullout_num)}')
    #print(f'난수 = {pick}')
    
    #for i in range()
    if pick in set(pullout_num):
        #print('당첨')
        return True
    #else:
        #print('꽝')
# ==========================================================

# 《데미지 판정 처리》

# 공격받음 판정 처리 -> 데미지 처리 -> 데미지 후처리


# 《데미지 처리 과정》

#   선공권 우선순위가 어느 쪽이 위인가?
#   피격 받았는가?  (Y/N)
#   특정 상태인가?  (노말/무적, 출혈 등등)
#   치명타가 터졌는가?  (Y/N)
#   데미지를 공식에 따라 계산
#   다시 노말 상태로 복귀



# 《데미지 공식》

# 명중했는가? (Y/N)
# 치명타가 터졌는가? (Y/N)
# 데미지 계산 = 현재 체력 - [{공격력 * (치명타 배율)} - (방어력 * )] * (피해 감소율)

# [계산 실험]

# 공격력 25, 방어력 20, 치명타 배율 1.2, 치명타 x
# = 25 * {1 - (0.01 * 20)} 
# = 20의 최종 데미지

# 공격력 30, 방어력 88, 치명타 배율 1.2, 치명타 o
# = (30 * 1.2) * {1 - (0.01 * 88)} 
# = 20의 최종 데미지




# 《데미지 후처리 과정》

#   받은 대상의 Hp가 0인가?
#       맞으면 사망처리
#       아니면 데미지만 받은 처리


# 《드랍 처리》

# 랜덤으로 아이템을 드랍
# 아이템 등급에 따라 드랍률을 달리한다


# ==========================================================

class Character:
    
    # 캐릭터 스테이터스 설정
    
    # 체력
    hp = 0
    # 마나
    mp = 0
    # 공격력
    atk = 0
    # 방어력
    dfn = 0
    # 마법 저항력
    res = 0.0
    # 치명타 확률
    ctr = 0.0
    # 치명타 배율
    cth = 1.5
    # 명중률
    cct = 1.0
    # 회피율
    agl = 0.0
    # 공격 우선권
    prior = 1
    
    
    # 장비 스테이터스 설정
    
    # 추가 체력
    add_hp = 0
    # 추가 마나
    add_mp = 0
    # 추가 공격력
    add_atk = 0
    # 추가 방어력
    add_dfn = 0
    # 추가 마법 저항력
    add_res = 0.0
    # 추가 치명타 확률
    add_ctr = 0.0
    # 추가 치명타 배율
    add_cth = 1.5
    # 추가 공격 우선권
    add_prior = 2
    
    
    # 총 스테이터스 설정
    
    # 체력
    #total_hp = 0
    # 마나
    #total_mp = 0
    # 공격력
    #total_atk = 0
    # 방어력
    #total_dfn = 0
    # 마법 저항력
    #total_res = 0
    # 치명타 확률
    #total_ctr = 0
    # 치명타 배율
    #total_cth = 0
    # 추가 공격 우선권
    #total_prior = 0

    
    # 디버프창
    debuff = []

    # 버프창
    buff = []

    # 칭호
    title = '없음'

    # 판정
    status = 'normal'
    
    # 장비
    equipment = []
    
    # 인벤토리
    inventory = []
    
    # 스킬
    skill = []
    
    # 드랍템
    drops = []
    rare_drops = []
    unique_drops = []

    
    
    # 초기화
    def __init__(self, name):
        self.name = name
        self.hp
        self.mp
        self.atk
        self.dfn
        self.res
        self.status
        self.ctr
        self.cth
        self.cct
        self.agl
        self.prior

    # 자신의 최종 스텟 업데이트
    def update_status(self):
        self.total_hp = self.hp + self.add_hp
        self.total_mp = self.mp + self.add_mp
        self.total_atk = self.atk + self.add_atk
        self.total_dfn = self.dfn + self.add_dfn
        self.total_res = self.res + self.add_res
        self.total_ctr = self.ctr + self.add_ctr
        self.total_cth = self.cth + self.add_cth
        self.total_prior = self.prior + self.add_prior


    # 공격
    def attack(self,enemy):
        
        # 공격 피격판정 처리
        enemy.status = 'attacked'
        damaged = self.total_atk
        
        # 무적 판정 처리
        if self.status == 'invincible':
            damaged = 0
            
        # 데미지 처리
        enemy.total_hp = enemy.total_hp - damaged

        if enemy.total_hp <= 0:
            enemy.total_hp = 0
            enemy.status == 'dead'
            print(f'{self.name}의 공격! / {self.total_atk} 데미지! /{enemy.name}의 남은 체력: {enemy.total_hp}')
            print(f'{enemy.name} 사망')
        
        # 데미지 후처리
        if enemy.total_hp == 0:

            drop_items = []
            number_values = []
            drop_tables = []

            # 노말은 여러개 나오기 때문에, drop_items를 이용한 정제 루트를 거쳐야 한다
            roll = rn.choices(enemy.drops, k = 5)
            for normal_items in roll:
                drop_items.append(normal_items)

            rare_chance = percent(20)
            #print(rare_chance)

            if rare_chance:
                roll_rare = rn.choice(enemy.rare_drops)
                drop_tables.append(roll_rare)
                #print(drop_tables)

            unique_chance = percent(5)
            print(unique_chance)

            if unique_chance:
                roll_unique = rn.choice(enemy.unique_chance)
                drop_tables.append(roll_unique)
                #print(drop_tables)

            # 겹치는 아이템 숫자 처리
            notUnique = set(drop_items)

            for list in notUnique:
                refine_num = drop_items.count(list)
                number_values.append(refine_num)

                if refine_num == 1:
                    refine_counts = list
                else:
                    refine_counts = f'{list} x{refine_num}'

                drop_tables.append(refine_counts)

            #print(f'드랍 템: {drop_items}')
            #print(f'각 갯수: {number_values}')
            #print(f'드랍 아이템: {drop_tables}')

            # drop_table 에 은화 추가
            coin_drops = f'{enemy.coins} 은화'
            drop_tables.append(coin_drops)

            # drop_table 출력

            print('┌'+'─'+'드롭 아이템' + '─' * 50 + '┐')
            print(*drop_tables, sep = ', ')
            print('└'+'─' * 62 + '┘')


        else:
            print(f'{self.name}의 공격! / {self.total_atk} 데미지! /{enemy.name}의 남은 체력: {enemy.total_hp}')
            enemy.status = 'normal'
    
    
    # 스킬 공격
    def skill_attack(self,enemy,num):
        
        # 공격 피격판정 처리
        enemy.status = 'attacked'
        damaged = self.skill[num]['damage']
        
        # 무적 판정 처리
        if self.status == 'invincible':
            damaged = 0
        
        # 데미지 처리
        enemy.total_hp = enemy.total_hp - damaged

        if enemy.total_hp <= 0:
            enemy.total_hp = 0
            enemy.status = 'dead'
            print(f'{self.name}의 스킬: {self.skill[num]['name']} 공격! / {self.skill[num]['damage']} 데미지! / {enemy.name}의 남은 체력: {enemy.total_hp}')
            print(f'{enemy.name} 사망')
        
        else:
            enemy.status = 'normal'
            print(f'{self.name}의 스킬: {self.skill[num]['name']} 공격! / {self.skill[num]['damage']} 데미지! / {enemy.name}의 남은 체력: {enemy.total_hp}')


        # 데미지 후처리
        if enemy.hp == 0:

            drop_items = []
            number_values = []
            drop_tables = []

            # 노말은 여러개 나오기 때문에, drop_items를 이용한 정제 루트를 거쳐야 한다
            roll = rn.choices(enemy.drops, k = 5)
            for normal_items in roll:
                drop_items.append(normal_items)

            # 레어 드랍확률
            rare_chance = percent(20)
            # print(rare_chance)

            if rare_chance:
                roll_rare = rn.choice(enemy.rare_drops)
                drop_tables.append(roll_rare)
                #print(drop_tables)

            # 유니크 드랍확률
            unique_chance = percent(5)
            # print(unique_chance)

            if unique_chance:
                roll_unique = rn.choice(enemy.unique_drops)
                drop_tables.append(roll_unique)
                #print(drop_tables)

            # 겹치는 아이템 숫자 처리
            notUnique = set(drop_items)

            for list in notUnique:
                refine_num = drop_items.count(list)
                number_values.append(refine_num)

                if refine_num == 1:
                    refine_counts = list
                else:
                    refine_counts = f'{list} x{refine_num}'

                drop_tables.append(refine_counts)

            #print(f'드랍 템: {drop_items}')
            #print(f'각 갯수: {number_values}')
            #print(f'드랍 아이템: {drop_tables}')

            # drop_table 에 은화 추가
            coin_drops = f'{enemy.coins} 은화'
            drop_tables.append(coin_drops)

            # drop_table 출력

            print('┌'+'─'+'드롭 아이템' + '─' * 50 + '┐')
            print(*drop_tables, sep = ', ')
            print('└'+'─' * 62 + '┘')
            
        else:
            enemy.status = 'normal'



class Goblin(Character):

    # 스테이터스 설정
    hp = 100
    mp = 0
    atk = 10
    dfn = 0
    
    # 드랍 테이블
    drops = ['고블린의 귀','고블린의 이빨']
    rare_drops = ['고블린의 귀걸이','고블린의 몽둥이']
    unique_drops = ['고블린의 이상한 반지']

    # 돈
    coins = rn.randrange(1,16)



    # 기본상태: 노말
    status = 'normal'

    # 초기화
    def __init__(self, name):
        self.name = name
        self.update_status()




class Player(Character):

    # 스테이터스 설정
    hp = 100
    mp = 100
    atk = 20
    dfn = 15
    title = '초보 플레이어'
    
    # 기본상태: 노말
    status = 'normal'

    # 스킬
    skill = [{'name':'강타','hp_cost':0, 'mp_cost':30, 'damage':100},
             {'name':'기습','hp_cost':0, 'mp_cost':25, 'damage':40, 'debuff_name': '출혈', 'debuff_damage': atk * 0.1, 'debuff_duration': 5},
             {'name':'독바른 검','hp_cost':0, 'mp_cost':45, 'damage':50, 'debuff_name': '중독','debuff_damage': atk * 0.3, 'debuff_duration': 2}
             ]
             
    
    # 초기화
    def __init__(self, name):
        self.name = name
        self.update_status()

# ==========================================================


# 객체 생성
goblin = Goblin('고블린')
player = Player('플레이어')


# ==========================================================

print('='*20)

# 공격, 사망판정 테스트

# 일반공격 3회
player.attack(goblin)

print('='*20)
time.sleep(0.5)

player.attack(goblin)

print('='*20)
time.sleep(0.5)

player.attack(goblin)

print('='*20)
time.sleep(0.5)

# 스킬 공격 1회
player.skill_attack(goblin,0)

print('='*20)

print(f'현재 플레이어의 상태: {player.status}')
print(f'현재 고블린의 상태: {goblin.status}')
print('='*20)


# 플레이어 스테이터스 창


print(' ')
print(f'이름 : {player.name}')
print(f'칭호 : 『{player.title} 』')
print(f'체력 : {player.hp}')
print(f'마나 : {player.mp}')
print(f'공격력 : {player.atk}')
print(f'방어력 : {player.dfn}')
print(f'치명타 확률: {round(player.ctr * 100)} %')
print(f'치명타 배율: {round(player.cth * 100)} %')
print(' ')
print(f'스킬목록 :')
print(f'ㄴ{player.skill[0]['name']}: {player.skill[0]['damage']} 데미지[마나: {player.skill[0]['mp_cost']}]')
print(f'ㄴ{player.skill[1]['name']}: {player.skill[1]['damage']} 데미지[마나: {player.skill[1]['mp_cost']}][{player.skill[1]['debuff_name']}: {int(player.skill[1]['debuff_damage'])} 데미지, 지속시간 {int(player.skill[1]['debuff_duration'])}초]')
print(f'ㄴ{player.skill[2]['name']}: {player.skill[2]['damage']} 데미지[마나: {player.skill[2]['mp_cost']}][{player.skill[2]['debuff_name']}: {int(player.skill[2]['debuff_damage'])} 데미지, 지속시간 {int(player.skill[2]['debuff_duration'])}초]')
print('='*20)


# 맵 설명
#print('■□□□□□□□□□□□■□\n■■■■■□■■■□■■■□\n□□□□■■■□■□■□□□\n□□□□■□□□■■■□□□\n■■■■■□□□□□■■■■')