# 4
def getGrade(score):
    return ("A" if score >= 90 else 
            "B" if score >= 80 else 
            "C" if score >= 60 else "F")


sco_ip = int(input("점수를 입력"))
result = getGrade(sco_ip)
print(f"당신의 점수 {sco_ip}, 학점 {result}")