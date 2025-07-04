import math

try:

    x1, y1 = map(float, input("첫 번째 점의 좌표 (x y) 를 입력하세요 : ").split())
    x2, y2 = map(float, input("두 번째 점의 좌표 (x y) 를 입력하세요 : ").split())
    # print(f"입력한 두 점 : ({x1}, {y1}), ({x2}, {y2}) 입니다.")

    x_minu = abs(x1 - x2)**2
    y_minu = abs(y1 - y2)**2

    total = math.sqrt(x_minu + y_minu)

    print(f"두 점의 거리는 {total}")
except ValueError:
    print("숫자가 아닌 값을 입력했습니다.")
