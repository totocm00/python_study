# 14
# 2와 20 사이에 있는 모든 소수를 찾는 프로그램
# (예제 7은 소수, 자신과 1만이 약수) 나누었을 때 몫이 0
minority = []
for i in range(2,21):
    if i % i== 0:
        if i % 2 != 0 and i % 3 != 0:
            minority.append(i)
print(minority)