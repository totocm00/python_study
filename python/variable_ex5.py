#Fahrenheit 화씨
#Celsius 섭씨
try:
    user_input = (input("화씨의 온도는? : "))

    if user_input.strip() == "":
        raise ValueError("입력이 비어있습니다.")

    heit = float(user_input)

# 온도 범위 제한 (예: 절대온도 아래 방지)
    if heit < -459.67:
        raise ValueError("화씨 온도는 절대영도(-459.67F)보다 낮을 수 없습니다.")

    cel = (heit - 32.0) * (5/9)
    msg = "화씨 %2.f°F -> 섭씨%2.f°F 입니다"
    print(msg % (heit, cel))

except ValueError as e:
    print(f"입력 오류: {e}")