# 표준 체중 = (키-100) x 0.9
# user_high, user_weight = map(float, input("키와 몸무게를 입력하세요 : (키 몸무게)").split())
user_high = float(input("키를 입력하세요: "))
stand_weight = (user_high - 100) *0.9
stand_low_weight = stand_weight *0.95
stand_high_weight = stand_weight *1.05

print(f"당신의 키{user_high}cm 가 평균이려면")
print(f"{stand_low_weight:.1f} ~ {stand_high_weight:.1f} 사이 몸무게 \n")

user_weight = float(input("몸무게를 입력하세요: "))

if stand_low_weight > user_weight:
    print("저체중입니다")
elif stand_high_weight < user_weight:
    print("과체중입니다")
else:
    print("평균입니다")