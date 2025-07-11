# 속담
import random

proverbs = [
    ["가까운","무당보다 먼 데 무당이 영하다"],
    ["긁어","부스럼"],
    ["경점 치고","문지른다"],
    ["꼬리가 길면","밟힌다"],
    ["내 일 바빠","한댁 방아"],
    ["망건 골에","앉았다"],
    ["석류는 떨어져도 안 떨어지는","유자를 부러워하지 않는다"],
    ["호박 덩굴이","벋을 적 같아서야"],
    ["이 열 번 물어도","모르면 송구하다"],
    ["죽 쑤고","개가 웃는다"],
    ["호랑이의 새끼를","만들지 않는다"]
]

correct = 0
for i in range(5):

    quiz = random.choice(proverbs)
    front, back = quiz

    while True:
        lie1, lie2 = random.choice(proverbs)
        if front != lie1:
            break

    front_or_back = random.choice(quiz)

    print(f"문제{i+1} :  {front_or_back}")

    if front_or_back == front:
        front = back

    list_a = [front,lie1]
    random.shuffle(list_a)

    print(f"1.{list_a[0]}\n2.{list_a[1]}")
    user_input = int(input("이어질 속담을 선택하세요: 1, 2 "))

    result = ""
    if user_input == 1:
        result = list_a[0]
    else:
        result = list_a[1]

    if result == front or result == back:
        correct += 1
        print("\t정답입니다")
    else:
        print("\t틀렸습니다")
    print("---------------------")
    
print(f"5문제 중 {correct}개 정답")