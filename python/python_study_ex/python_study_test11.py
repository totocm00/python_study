# 정의되는 함수값을 계산.
# 사용자로부터 x값을 입력받아 계산.
# X는 실수
# f(x) = { x**2 - 9x + 2    x<=0
#        { 7x + 2           x>=0
user_float_input = float(input("x : 실수 값을 입력하세요 "))
answer_float = 0
if user_float_input <= 0:
    answer_float = user_float_input**2 - 9*user_float_input + 2
else:
    answer_float = 7*user_float_input + 2
print(f"답은 {answer_float:.2f} 이다. 소숫점 2번째 까지 출력")