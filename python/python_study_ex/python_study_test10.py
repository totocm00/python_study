print("test4")
import random

# 1. 랜덤으로 덧셈, 뺄셈, 곱셈, 나눗셈을 하나의 함수에 담는다
# 2. 두 정수값을 랜덤으로 생성하여 문제를 만든다 // 총 3가지 랜덤
# 3. 사용자로부터 답을 입력받아 정답 혹은 오답을 판단하는 프로그램
random.seed()
operator_random = random.randint(1,4)
# operator_fx = ""
# if operator_random == 1:
#     operator_fx = "+"
# elif operator_random == 2:
#     operator_fx = "-"
# elif operator_random == 3:
#     operator_fx = "*"
# elif operator_random == 4:
#     operator_fx = "/"
# print(f"램덤으로 뽑힌 연산자는 {operator_fx} 입니다")

#key : value 딕셔너리 형태
# key 값은 +, -, *, / 의 문자열
# value 는 람다식
print("test3")
operations = {
    "+" : lambda a, b: a + b,
    "-" : lambda a, b: a - b,
    "*" : lambda a, b: a * b,
    "/" : lambda a, b: a / b
    if b != 0
    else "나눗셈 오류"
}
# 랜덤 연산자를 선택 // random.choice는 list 형태로 받음
# 자료형변환으로 오퍼레이션.키즈를 딕셔너리에서 리스트로 바꿔줌
print("test2")
operator_fx = random.choice(list(operations.keys()))
integer_random_one, integer_random_two = [random.randint(1, 10) for _ in range(2)]
msg = f"{integer_random_one} {operator_fx} {integer_random_two} = ?"
print(msg + "안나올 때 무슨 결과인지 test용1")
print(f"one 0{integer_random_one}",f"two {integer_random_two}",f"fx {operator_fx} \n" )
print(msg)

answer = operations[operator_fx](integer_random_one, integer_random_two)
if float(answer) == 1:
    "{answer} = {answer}:.2f"

try:
    user_correct = float(input("답을 적어주세요 : "))

    if isinstance(answer, str):
        print("계산할 수 없는 문제 - 나눗셈 오류")
    elif operator_fx == "/" and abs(user_correct - answer) < 0.01:
        print(["*" for _ in range(5)])
        print("정답!")
    elif user_correct == answer:
        print(["정답" for _ in range(3)])
        print("정답임!")
    else:
        print(f"오답입니다. 정답 {answer}")
except ValueError:
    print("숫자만 입력하세요")