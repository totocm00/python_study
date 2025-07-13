import random
import time

BOOM_LIST = [
    "참외", "수박", "토끼", "의자", "컴퓨터", 
    "자동차", "사자", "초콜릿", "연필", "강아지",
    "노트북", "냉장고", "포도", "커피", "바나나",
    "비행기", "바다", "펜", "신발", "달력"
]

GAME_START_MSG_MENT = "게임을 시작합니다"
GAME_START_MSG_C_THREE = "3"
GAME_START_MSG_C_TWO = "2"
GAME_START_MSG_C_ONE = "1"
GAME_START_MSG_C_START = "START"
TIME_ONE_SEC = 1
LIFE_DIFAULT_VALUE = 3


life = 3
score = 0
limit_time = 2

# 유저한테 인풋
def user_input():
    return input("단어 입력")

# 랜덤 단어를 출력
def random_output(boom_list):
    random.shuffle(boom_list)
    return random.choice(boom_list)

# 생명 생성
def generate_life_default(n):
     return n

# 생명이 0인지 체크
def life_zoro_check(life):
    if life == 0:
        return True
    return False

# 폭탄단어와 유저입력이 같은지 체크
def boomAndInput_check(boom,userInput):
    if boom == userInput:
        return True
    return False

# 타이머
def time_two_second(n):
    timeout = n # 60에 1분
    start = time.time()
    while time.time() - start < timeout:
	    pass
print("타임어택 종료!")



print(GAME_START_MSG_MENT)

print(GAME_START_MSG_C_THREE)
time_two_second(TIME_ONE_SEC)

print(GAME_START_MSG_C_TWO)
time_two_second(TIME_ONE_SEC)

print(GAME_START_MSG_C_TWO)
time_two_second(TIME_ONE_SEC)

print(GAME_START_MSG_C_ONE)
time_two_second(TIME_ONE_SEC)

print(GAME_START_MSG_C_START)
time_two_second(TIME_ONE_SEC)

# 붐리스트 생성
random_output(BOOM_LIST)
# 생명 생성
generate_life_default(LIFE_DIFAULT_VALUE)












