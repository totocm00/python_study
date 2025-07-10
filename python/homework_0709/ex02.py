# 2
myList = [11, 22, 23, 99, 81, 93, 35]
answer = 0
for i in range(len(myList)):
    answer += myList[i]
print(answer)


# refactor
sum = 0
for i in range(myList):
    sum += i

print("정수들의 합은", sum)