# 11
# 사용자가 2개의 정수(a와 b)를 입력하면 이들 정수의 최대 공약수를 찾아라.
# 예를 들어 3과 6의 최대 공약수는 3.

def common_divisor(one, two):
    one_two_cd = 1
    for i in range(1, min(one, two) + 1):
        if one % i == 0 and two % i == 0:
            one_two_cd = i
    return one_two_cd

one_ip, two_ip = map(int, input("정수 2개 입력 :(x y)").split())
print(f"{one_ip}와 {two_ip}의 최대공약수는 {common_divisor(one_ip, two_ip)}")


# 유클리드 호제법
# python의 동시할당(multiple assignment) 사용
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
x, y = map(int, input("정수 2개 입력: ").split())
print(f"{x}와 {y}의 최대공약수는 {gcd(x, y)}입니다.")

# 오른쪽 b와 a%b 를 먼저 계산
# 그 결과를 동시에 왼쪽 변수와 a와 b에 할당
# temp = a
# a = b
# b = temp % b


# a = 48
# b = 18
# a, b = b, a % b

# a, b = 18, 12   # 48 % 18 = 12
# a, b = 12, 6    # 18 % 12 = 6
# a, b = 6, 0     # 12 % 6 = 0 → b가 0이므로 종료


# a % b = 48 % 18 = 12
# a 는 b의 값 18을 받고
# b는 a % b의 결과 12를 받음
# 1. a, b = 48, 18 → 48 % 18 = 12 → 다음 단계로
# 2. a, b = 18, 12 → 18 % 12 = 6 → 다음
# 3. a, b = 12, 6 → 12 % 6 = 0 → 끝!