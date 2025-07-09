# 4
user_input_integer = int(input())

multiple_x = ""
for i in range(1,user_input_integer + 1):

    if user_input_integer % i == 0:
        multiple_x += str(i) + " "
print(multiple_x)