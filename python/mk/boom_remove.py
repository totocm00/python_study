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