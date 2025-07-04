user_input = input("네 자리의 정수를 입력하세요 : ")

count = 0
for i in range(0, len(user_input)):
    count += int(user_input[i])

# fourth = num//1000
# print(fourth)
# third = (num%1000)//100
# second = (num%100)// 10
# first = (num%10)
# sum = forth + third + second + first

print(f"네 자리수의 합은 : {count} 입니다")