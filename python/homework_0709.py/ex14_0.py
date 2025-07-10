# 14
# 2와 20 사이에 있는 모든 소수를 찾는 프로그램
# (예제 7은 소수, 자신과 1만이 약수) 나누었을 때 몫이 0

maxNum = 20
number = 2
count = 0

# divisor 약수
# prime 소수
# while 문 안에 while문을 쓰는 것은 위험함
# 계속 반복해서 프로그램이 죽어버릴 수 있음
while number < maxNum:
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor +=1
    if prime:
        count+=1
        print(number,end=" ")
    number += 1

# while문 -> for문
for i in range(2,maxNum+1):
    divisor = 2
    prime = True

    #while divisor<number:
    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
            break
        #divisor +=1
    
    if prime:
        count+=1
        print(number, end=" ")
    number+=1


# 배열로 작성

minority = []
for i in range(2,21):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        minority.append(i)
print(minority)