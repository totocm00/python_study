import random

random.seed()
operator_random = random.randint(1,4)

# random.random -> 아무 숫자나 뽑아줌
# random.randint(a,b) -> a ~ b 까지 무작위

# random.ranrange(a,b,c) -> a ~ b 까지 스텝을 줌 range
# random.ranrange(1,10) -> 1 ~ 9 까지임 : 0부터 계산하기 때문에 끝에 한 자리가 누락된다.
# rando,.randint(1,10) -> 1 ~ 10 까지임.

# random.randint 에 0,10 의 경우에
# 값에 0이 나오면 계속 계산을 하기 때문에 컴퓨터의 무리가 가고
# 특수한 케이스에 걸리게 된다.

operations = {
    "+" : lambda a, b: a + b,
    "-" : lambda a, b: a - b,
    "*" : lambda a, b: a * b,
    "/" : lambda a, b: a / b
    if b != 0
    else "나눗셈 오류"
}

x = 0
match x:
    case 1: 
        print("정답")
    case 2:
        print("오답")


# key : value 딕셔너리 형태
# key 값은 +, -, *, / 의 문자열
# value 는 람다식

operator_fx = random.choice(list(operations.keys()))
# 랜덤 연산자를 선택 // random.choice는 list 형태로 받음
# 자료형변환으로 오퍼레이션.키즈를 딕셔너리에서 리스트로 바꿔줌

integer_random_one, integer_random_two = [random.randint(1, 10) for _ in range(2)]
msg = f"{integer_random_one} {operator_fx} {integer_random_two} = ?"

print(msg)

answer = operations[operator_fx](integer_random_one, integer_random_two)

try:
    user_correct = float(input("답을 적어주세요 : "))

    if isinstance(answer, str):
        print("계산할 수 없는 문제 - 나눗셈 오류")

# isinstance("hello", str)      # True
# isinstance(3.14, float)       # True
# isinstance(42, int)           # True
# isinstance([1, 2, 3], list)   # True
# isinstance("123", int)        # False


    elif operator_fx == "/" and abs(user_correct - answer) < 0.01:
        print("정답!")
    elif user_correct == answer:
        print("정답임!")
    else:
        print(f"오답입니다. 정답 {answer}")
except ValueError:
    print("숫자만 입력하세요")