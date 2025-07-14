user_input = []
user_input = map(int, input("정수 다섯개 입력:(a b c b e)").split())
input_set = set(user_input)
user_input = sorted(input_set)
print(user_input)
print(type(user_input))