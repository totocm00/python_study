# 9
def print_str_list(input_iput):
    answer_list = list(set(input_iput[0]) & set(input_iput[1]))
    print(answer_list)

input_iput = list(map(str, input("문자열을 두 개 입력: (x y):").split()))
# result_list = [x for x in input_iput[0] if x in input_iput[1]] # lost_first
# print(result_list)

# result_list_second = [x for x in input_iput[1] if x in input_iput[0]] 
# reslut = result_list_first + result_list_second -> 겹치지 않는 것들

print_str_list(input_iput)