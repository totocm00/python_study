# 8
# while을 사용하여 n**2 > 500 인 n 중에서 가장 작은 n을 찾는 프로그램
n = 1
while 1:
    if n * n > 500:
        break
    n += 1
print(f"1. 가장 작은 n은 {n}")

w = 1
while w * w <= 500:
    w += 1
print(f"2. 가장 작은 w은 {w}")


# refactor
# while n<500:
#     if (n**2) > 500:
#         print(n)
#         break
#     n+=1

# while n<500:
#     if pow(n,2) > 500:
#         print(n)
#         break
#     n+=1