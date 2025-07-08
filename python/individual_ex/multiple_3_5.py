# 사용자로부터 정수를 받아서 3의 배수이면 "Python" 를 출력한다
# 만약 5의 배수이면 "Express"을 출력한다.
# 만약 3의 배수이면서 5의 배수이면 "Python Express"를 출력한다

def check_multiple(num):
    result = ""
    if num % 3 == 0:
        result += "Python "
    if num % 5 == 0:
        result += "Express"
    print(result.strip() if result else "정수를 입력하세요")

integer_input = int(input())
check_multiple(integer_input)

# strip() 는 문장 양 끝의 공백을 제거한다
# <A> if <조건> else <B>  ->  조건이 참이면 A, 아니면 B 반환
# A와 B에는 내가 만든 함수를 비교식으로 넣어도 가능하다
# 간단한 내용은 삼항연산자로 표현하면 간결하지만
# 긴 내용은 가독성을 해치기 때문에 비추천