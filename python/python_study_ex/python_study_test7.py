# a, b, c = eval (input("3개의 정수를 입력하시요: "))

x6, x7, x8 = map(int, input("세 정수를 입력하세요 (x y z)").split())
min_num = 0
if(x6 < x7):
    min_num = x6
else:
    min_num = x7
if(min_num > x8):
    max_num = x8
    
print(f"가장 작은 값은 {min_num}")