# 속담
import random

proverbs = [
    ["굴러온 돌이","박힌 돌 뺀다"],
    ["긁어","부스럼"],
    ["돼지에","진주 목걸이"],
    ["꼬리가 길면","밟힌다"],
    ["돌다리도","두들겨 보고 건너라"],
    ["마른하늘에","날벼락"]
]

quiz = random.choice(proverbs)
front, back = quiz

while True:
    lie1, lie2 = random.choice(proverbs)
    if front != lie1:
        break

front_or_back = random.choice(quiz)

print(f"문제 :{front_or_back}")

if front_or_back == front:
    front = back

list_a = [front,lie1]
random.shuffle(list_a)

print(f"1.{list_a[0]}  2.{list_a[1]}")
user_input = int(input("이어질 속담을 선택하세요: 1, 2 "))

result = ""
if user_input == 1:
    result = list_a[0]
else:
    result = list_a[1]

if result == front or result == back:
    print("정답입니다")
else:
    print("틀렸습니다")