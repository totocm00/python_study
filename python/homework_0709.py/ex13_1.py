# 13 -1


# 사용자로부터 정수 입력
n = int(input("피보나치 수열을 몇 번째(n)까지 출력할까요? "))

# 초기 피보나치 수열 정의
f0 = 0
f1 = 1

# 출력 시작
print("피보나치 수열:")

for i in range(n + 1):  # 0부터 n까지 포함되도록 n+1
    if i == 0:
        print(f0, end=' ')
    elif i == 1:
        print(f1, end=' ')
    else:
        fn = f0 + f1
        print(fn, end=' ')
        f0 = f1  # 이전 값 업데이트
        f1 = fn  # 현재 값 업데이트