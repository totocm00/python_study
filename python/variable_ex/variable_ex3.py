# 삼각형 두 변의 길이는 합이 항상 나머지 한 변보다 커야한다
#a + b > c
#a + c > b
#b + c > a
''' 가장 작은 변을 구하려면 abs를 써야한다 |a - b| < c
    !두 변의 차보다 커야한다!

    min이 왜 안되느냐?
    a = 10, b = 2 이면
    min(a, b) = 2
    세 번째 변을 c = 2라고 잡으면?
    검사 : a + b = 12, |a - b| = 8
    조건 : |a - b| < c -> 8 > 2  ==> false
    c 가 무조건 두 변의 차보다 커야 삼각형이 됨

    abs(a - b) = |10 - 2| = 8
    그래서 abs(a-b) + 1을 사용해서 구해줘야 한다.
'''

tri1 = float(input("삼각형의 첫번째 변의 길이 입력 : "))
tri2 = float(input("삼각형의 두번째 변의 길이 입력 : "))
maxTri3 = (tri1+tri2)-1
msg = "나머지 변의 최대 길이는 %.1f 입니다."

if tri1 <= 0 or tri2 <= 0:
    print("변의 길이는 0보다 크게 입력하세요")
else:
    maxTri3 = tri1 + tri2 - 1
    print(msg % maxTri3)