import random
random.seed()
com = random.randint(1,3)
fiteCom = ""
if com == 1:
    fiteCom = "가위"
if com == 2:
    fiteCom = "바위"
if com == 3:
    fiteCom = "보"

x9 = input("가위 바위 보 중 하나를 입력하세요 : ")

userNum = 0
if x9 == "가위":
    userNum = 1
elif x9 == "바위":
    userNum = 2
elif x9 == "보":
    userNum = 3
else:
    print("가위 바위 보 입력이 아닙니다.")

result = 0
drow = "비김"
if userNum == com:
    print(drow)
elif (userNum == 1 and com == 3) or (userNum == 2 and com == 1) or (userNum == 3 and com == 2):
    print("사람 승리")
else:
    print("컴퓨터 승리")
