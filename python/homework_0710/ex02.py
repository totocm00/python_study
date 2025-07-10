# 2
def sum_1(input1, input2):
    return input1 + input2

def minu_1(input1, input2):
    return input1 - input2

def mul_1(input1, input2):
    return input1 * input2

def vag_1(input1, input2):
    return input1 / input2

input1, input2 = map(int, input("두 숫자 입력: (x y)").split())
print(sum_1(input1,input2))
print(minu_1(input1,input2))
print(mul_1(input1,input2))
print(vag_1(input1,input2))