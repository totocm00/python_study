# 10
# 1**2 + 2**2 + 3**2 + 4**2 ... n**2 의 값을 계산하여 출력

n_input = int(input("n 값 입력 : "))
sum_twoSquared = 0
i = 1
while i <= n_input:
    sum_twoSquared += i * i
    i += 1
print(f"1. 1부터 {n_input}까지의 제곱의 합 : {sum_twoSquared}")


sum_squared = 0
for vv in range(1, n_input +1):
    sum_squared += vv * vv
print(f"2. 1부터 {n_input}까지의 제곱의 합 : {sum_squared}")

# 자연수 제곱합 공식 ( 수학 공식 버전)
# 1**2 + 2**2 + 3**2 + ... + n**2
# n(n + 1)(2n + 1)
#------------------
#        6
# --> n *(n+1) * (2*n+1) // 6   # 정수 나눗셈
n = n_input
sum_fast = n *(n+1) * (2*n+1) // 6
print(f"3. 1부터 {n}까지의 제곱의 합 : {sum_fast}")