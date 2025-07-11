import random
import time

boom_list = [
    "참외", "수박", "토끼", "의자", "컴퓨터", 
    "자동차", "사자", "초콜릿", "연필", "강아지",
    "노트북", "냉장고", "포도", "커피", "바나나",
    "비행기", "바다", "펜", "신발", "달력"
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