import random
import time

'''
ReadMe:

<h3 or 4>
1. 게임이 시작 될 때 필요한 부분들을 생성.
    - 폭탄리스트, 매 판 새로운 순서-> 셔플로 리스트 재생성, 생명, 타이머 생성,
      생명체크(생명 0이면 False 로 반복문 종료시키도록),

2. while을 함수로 만들면 안의 내용도 집어 넣어야 하고
    받아서 사용하는 인자들이 많아지므로 while은 밖에서 만든다.

3. 게임 시작 멘트나 멘트들을 모아두는 함수를 생성 -> 상수로 변경되고 -> list로 변경되었음
      

</h4>


'''


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

GAME_START_SEQUENCE = [
    GAME_START_MSG_C_THREE,
    GAME_START_MSG_C_TWO,
    GAME_START_MSG_C_ONE,
    GAME_START_MSG_C_START
]


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

# 순서대로 메시지를 뱉아내도록 생성 
def game_star_msg():
    for msg in range(GAME_START_SEQUENCE[:-1]):
        print(msg)
        time_two_second(TIME_ONE_SEC)


# 붐리스트 생성
boom_list = random_output(BOOM_LIST)
# 생명 생성
human_life = generate_life_default(LIFE_DIFAULT_VALUE)












