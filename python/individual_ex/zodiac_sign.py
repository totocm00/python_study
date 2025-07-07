# 연도를 입력하면 띠를 출력하는 프로그램을 작성.
# 띠는 연도를 12로 나누어 결정
# 나머지가 0이면 원숭이띠, 1이면 닭띠, 2이면 개띠, ...11이면 양띠

year_input = int(input("연도 입력"))
zodiac_sign = ["원숭이", "닭", "개", "돼지", "쥐", "소",
               "호랑이", "토끼", "용", "뱀", "말", "양"]
input_zodiac = year_input % 12

print(zodiac_sign[input_zodiac] + "띠")