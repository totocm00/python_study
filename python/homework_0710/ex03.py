# 3번
import ex02 as ii
# 4개의 함수 호출
# 두개의 입력을 받고 동시에 수행해서
# 출력
def calc():
    a = ii.sum_1(input3,input4)        
    b = ii.minu_1(input3,input4)
    c = ii.mul_1(input3,input4)
    d = ii.vag_1(input3,input4)
    print(a,b,c,d)

input3, input4 = map(int, input("두 숫자 입력: (x y)").split())
calc()