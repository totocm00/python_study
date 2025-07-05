import random

random.seed()
operator_random = random.randint(1,4)

operations = {
    "+" : lambda a, b: a + b,
    "-" : lambda a, b: a - b,
    "*" : lambda a, b: a * b,
    "/" : lambda a, b: a / b
    if b != 0
    else "나눗셈 오류"
}

operator_fx = random.choice(list(operations.keys()))
integer_random_one, integer_random_two = [random.randint(1, 10) for _ in range(2)]
msg = f"{integer_random_one} {operator_fx} {integer_random_two} = ?"

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