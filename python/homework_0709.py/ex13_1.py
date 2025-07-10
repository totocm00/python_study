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

# refactor

num = int(input())
element1 = 0
element2 = 0

for i in range(num + 1):
    if i<2:
        element2 = element1
        element1 = i
        sum = element1 + element2
    else:
        sum = element1 + element2
        element2 = element1
        element1 = sum
    
    if i!=num:
        print(sum,end=",")
    else:
        print(sum)