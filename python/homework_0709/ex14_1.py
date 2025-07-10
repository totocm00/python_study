maxNum = 20        # 검사할 최대 숫자 (20까지 검사)
number = 2         # 검사 시작 숫자 (2부터 시작)
count = 0          # 소수의 개수를 세기 위한 변수

# number가 maxNum보다 작을 때까지 반복
while number < maxNum:
    divisor = 2     # 나눗셈을 시작할 첫 약수 (1은 생략하고 2부터 시작)
    prime = True    # 현재 number가 소수인지 판별할 변수

    # 2부터 number-1까지 나눠서 나누어떨어지면 소수가 아님
    while divisor < number:
        if number % divisor == 0:  # 나누어 떨어지면
            prime = False          # 소수가 아님
            break                  # 더 이상 검사할 필요 없음
        divisor += 1              # 다음 약수 검사

    if prime:  # 소수일 경우
        count += 1                # 소수 개수 +1
        print(number, end=" ")    # 소수 출력 (줄바꿈 없이 공백으로 구분)

    number += 1  # 다음 숫자로 이동

# 결과: 2와 20 사이의 소수 출력 (예: 2 3 5 7 11 13 17 19)