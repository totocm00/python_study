# 8

# 상수로 고정 값
# KOREAN_NUMS(한글매핑), UNITS(자릿수)
KOREAN_NUMS = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
UNITS = ["천", "백", "십", ""]

def convert_to_korean_money(amount):
    str_amount = str(amount)
    len_amount = len(str_amount)
    result = ""

    # 핵심
    # 슬라이싱으로 동적 제어해서 필요한 데이터만 쑉 뽑아 씀
    sliced_units = UNITS[-len_amount:]

    for i in range(len_amount):

        # 각각 배열의 i번째를 들고와서 비교함
        digit = int(str_amount[i]) # 현재 자리 숫자 123입력 -> "123" -> "1","2","3"
        unit = sliced_units[i] # 자릿수 단위 저장

        if digit == 0:     #일백 영 칠 (107) 이라고 안 읽으니까 0 = 영 을 뻄
            continue

        if digit == 1 and unit != "": # 일 생략함 숫자가 1이고 단위가 있다면 ex)일백 -> 백
            result += unit
        else:
            result += KOREAN_NUMS[digit] + unit
    return result

amount = int(input("숫자를 입력 (1~10000): "))
if 1 <= amount < 10000:
    print(f"숫자: {amount} 만원")
    print(f"한글: {convert_to_korean_money(amount)} 만원")
else:
    print("1부터 10000 사이의 숫자만 입력하세요.")
