#try 안의 조건문을 if로 감싸는 경우가 있을 때 빨간줄 그여서 밖에서 정의? 해줌
score = 0
msg = "잘 못 된 값입니다."
try:
    score = int(input("성적을 입력하시오: "))

    if score > 100:
        raise print("100점이하의 점수를 입력하세요")    

    if score >= 90:
        print("학점 A")
    elif score >= 80:
        print("학점 B")
    elif score >= 70:
        print("학점 C")
    elif score >= 60:
        print("학점 D")
    else:
        print("학점 F")
except ValueError:
    print(msg)