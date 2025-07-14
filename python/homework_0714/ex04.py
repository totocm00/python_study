# 4
def is_check_keyAndInput(key,value,user_input):
    if key == int(user_input):
        print(f"키값 : {key}, 입력한 값 : {user_input}")
        print(f"해당 키 값의 숨겨진 숫자는: {value}")

d = {1: 10, 2:20, 3:30, 4:40, 5:50, 6:60}
user_input = input()
# print(user_input)
# print(type(user_input))
for key, value in d.items():
    # print(key,type(key))
    is_check_keyAndInput(key,value,user_input)