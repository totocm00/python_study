# 5
# 중첩 반복문을 사용하여 입력된 정수만큼 *를 순차적으로 출력
input_x = int(input())
for i in range(1,input_x+1):
    for _ in range(i):
        print("*",end=" ")
    print()