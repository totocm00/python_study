# 6
import random
import time
print("번호를 누르면 해당하는 수에 맞춰서 동작합니다.")
user_correct_number = int(input("1.1~10랜덤수2개 2.1~100랜덤수2개 3.오늘날짜 월/일 2개"))
user_correct_math = int(input("실행할 연산 선택 : 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈"))

ran_ten = random.randint(1,10)
ran_hundred = random.randint(1,100)
now = time.localtime()
month = now.tm_mon
day = now.tm_mday

arithmetic_choice = [
    lambda a, b : a + b,
    lambda a, b : a - b,
    lambda a, b : a * b,
    lambda a, b : a / b if b != 0 else "0으로 나누기 x"
]

user_num_choice = []
if user_correct_number == 1:
    user_num_choice = [ran_ten for _ in range(2)]
if user_correct_number == 2:
    user_num_choice = [ran_hundred for _ in range(2)]
if user_correct_number == 3:
    user_num_choice = [month, day]

def make_math_quiz(input1,input2,oper_index):
    arith_choice = arithmetic_choice[oper_index -1]
    answer = arith_choice(input1,input2)
    print(f"문제: {input1} {'+ - * /'[oper_index-1]} {input2} = ?")
    print(f"정답: {answer}")
    
make_math_quiz(user_num_choice[0],user_num_choice[1],user_correct_math)