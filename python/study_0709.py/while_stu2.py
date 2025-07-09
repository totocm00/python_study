
# def multiple (num):
#     for i in range(num):
#         print("\n")
#         for j in range(num):
#             print("*",end=" ")

# try:
#     while 1:
#         try:
#             user_input = int(input("정수를 입력: "))
#             if isinstance(user_input,int):
#                 print(multiple(user_input))
#                 break
#         except ValueError:
#             print("에러")
        
# except ValueError:
#     print("정수를 입력하세요.")

# ------------------------------------

def multiple(num):
    for _ in range(num):
        print()  # 줄 바꿈
        for _ in range(num):
            print("*", end=" ")
    print()  # 마지막 줄 바꿈

while True:
    user_input = input("정수를 입력: ")
    try:
        number = int(user_input)
        multiple(number)
        break
    except ValueError:
        print("정수를 입력하세요.")
