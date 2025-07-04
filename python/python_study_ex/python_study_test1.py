age = int(input("나이를 입력하세요 : "))

if age > 20:
    print("성인입니다.")
elif age < 20 and age > 0:
    print("미성년자입니다")
else:
    print("잘 못 입력")