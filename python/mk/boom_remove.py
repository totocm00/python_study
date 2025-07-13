import random
import time

'''
ReadMe:

1. 게임이 시작 될 때 필요한 부분들을 생성.
    - 폭탄리스트, 매 판 새로운 순서-> 셔플로 리스트 재생성, 생명, 타이머 생성,
      생명체크(생명 0이면 False 로 반복문 종료시키도록),

2. while을 함수로 만들면 안의 내용도 집어 넣어야 하고
    받아서 사용하는 인자들이 많아지므로 while은 밖에서 만든다.

3. 게임 시작 멘트나 멘트들을 모아두는 함수를 생성 -> 상수로 변경되고 -> list로 변경되었음
      
### 추가 구현 기록
# 게임의 난이도 조정 1번째 맞추는 개수 생성 -( 이후 추가: 난이도 조절에서 시간을 줄이는 구현 예정 )
# 유저 생명력 default 값 부여 - ( 이후 추가 : 난이도 조절에서 라이프 개수를 줄이는 방법도 구현 예정)

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
TIME_TWO_SEC = 2
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

# 유저에게 단어를 받는 인풋
def input_user_word():
    return input()

# 유저에게 몇 레벨로 플레이할지 물어보는 인풋
def input_user_lever():
    print("플레이 할 단계를 선택하세요")
    print("1. LV1")
    print("2. LV2")
    print("2. LV3")
    return input()


# 랜덤 단어를 출력
def random_output(boom_list):
    return random.choice(boom_list)

# 랜덤 문장의 출력 순서를 변경해줌
def random_shuffle(boom_list):
    random.shuffle(boom_list)

# 생명 생성
def generate_life_default(n):
     return n

# 생명이 0인지 체크
def check_life_zoro(life):
    if life == 0:
        return True
    return False

# 폭탄단어와 유저입력이 같은지 체크
def check_boomAndInput(boom,userInput):
    if boom == userInput:
        return True
    return False

# 타이머
def time_two_second(n):
    timeout = n # 60에 1분
    start = time.time()
    while time.time() - start < timeout:
	    pass

# 순서대로 메시지를 뱉아내도록 생성 
def game_star_msg():
    for msg in range(GAME_START_SEQUENCE[:-1]):
        print(msg)
        time_two_second(TIME_ONE_SEC)

# 게임의 난이도 조정 1번째 맞추는 개수 생성 -( 이후 추가: 난이도 조절에서 시간을 줄이는 구현 예정 )
def choice_game_level(input_level):
    return 10 * input_level

# ---------------------------아래는 게임의 영역 ------------------




# 게임 시작시 순서를 섞어줌
random_shuffle(BOOM_LIST)

# 유저 생명력 default 값 부여 - ( 이후 추가 : 난이도 조절에서 라이프 개수를 줄이는 방법도 구현 예정)
human_life = generate_life_default(LIFE_DIFAULT_VALUE)

print()

level = choice_game_level(GAME_LEVEL_OEN)


for i in range(level):
    
    # 붐 단어를 뽑아옴 생성
    random_boom = random_output(BOOM_LIST)
    
    while True:
        print(f"")
        time_two_second(TIME_TWO_SEC)





        break










