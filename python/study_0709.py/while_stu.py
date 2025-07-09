score = 0
total_sum = 0
c = 0
print("종료하려면 음수값을 입력하세요.")

while score >= 0:
    score = int(input("정수를 입력하세요: "))
    if score > 0:
        total_sum += score
        c += 1
if c > 0:
    average = total_sum / c
    print("평균 점수는", average, "입니다")