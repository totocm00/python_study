# 15
# 다음 수열의 합을 계산
# 1/3 + 3/5 + 5/7 .... 99/101
origin_ip = int(input())

capy_i = 0
capy_two_gap = 0
capy_division_plus = 0
for i in range(1,origin_ip+1,2):
    capy_i = i
    capy_two_gap = i+2

    capy_division_plus += capy_i / capy_two_gap

    print(f" 입력 받은 수 {origin_ip}")
    print(f" {capy_i} / {capy_two_gap}")
print(f"앞의 수 합 {capy_i}")
print(f"뒤의 수의 합 {capy_two_gap}")
print(f"분수의 총 합은 {capy_division_plus:.2f}")