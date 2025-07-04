def is_float(s):
    try:
        return minu_float(s)
    except ValueError:
        return False

def minu_float(s):
    f = float(s) # 먼저 float로 바꾸고 바꿀 때 정수, 실수가 아니면 에러 터짐
    if(f < 0):
        return False
    else:
        return True

s = input("음식의 가격을 입력하세요 :").strip()
if is_float(s):
    cost = float(s)
    tip = cost * 0.1
    print(f"입력한 가격: {cost}, 지불할 팁: {tip:.0f}")
else:
    print("입력한 값이 유효하지 않습니다. (숫자 또는 양수 입력) ")