def solution(num_list):
    answer = 0
    temp = 1
    long_list = len(num_list)

    for i in range(long_list):
        if long_list <= 10:
            temp *= num_list[i]
        if long_list >= 11:
            answer += num_list[i]
    return temp if answer == 0 else answer