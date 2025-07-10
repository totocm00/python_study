# 17
# 0~9까지 정수 반복
# 특정숫자가 3으로 나눠 떨어지면 "Fizz" 출력
# 5로 나눠 떨어지면 "Buzz" 출력
# 3과 5로 나눠 떨어지면

def output_F_B(num):
    temp = ""
    for i in range(10):
        if i % 3 == 0:
            temp += "Fizz"
        if i % 5 == 0:
            temp += "Buzz"
        print(temp.strip() if temp else "*")

for i in range(10):
    temp = ""
    if i % 3 == 0:
        temp += "Fizz"
    if i % 5 == 0:
        temp += "Buzz"
    print(temp.strip()) if temp else "*"
