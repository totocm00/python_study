# 표준 체중 = (키-100) x 0.9
#user_high = float(input("키를 입력하세요: "))
#user_weight = float(input("몸무게를 입력하세요: "))
user_high, user_weight = map(float, input("키와 몸무게를 입력하세요 : (키 몸무게)").split())

stand_weight = (user_high - 100) *0.9

if stand_weight > user_weight:
    print("저체중입니다")
elif stand_weight < user_weight:
    print("과체중입니다")
else:
    print("평균입니다")