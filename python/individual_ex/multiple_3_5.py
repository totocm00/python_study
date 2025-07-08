# 사용자로부터 정수를 받아서 3의 배수이면 "Python" 를 출력한다
# 만약 5의 배수이면 "Express"을 출력한다.
# 만약 3의 배수이면서 5의 배수이면 "Python Express"를 출력한다

integer_input = int(input())
if integer_input % 3 == 0 and integer_input % 5 == 0:
    print("Python Express")
elif integer_input % 3 == 0:
    print("Python")
elif integer_input % 5 == 0:
    print("Express")
else:
    ("정수를 입력하세요")