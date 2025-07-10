# 5
# 패스워드 검증 함수 checkPass(p)
# 패스워드 적어도 8자 이상
# 적어도 1글자의 대문자와 소문자, 숫자가 들어가야하고 알파벳 한정
# 1글자 대문자,소문자,숫자
# 알파벳으로 구성

def checkPass(p):
    if len(p) < 8:
        return "8자 이상 입력하세요"
    is_num = False
    is_upper = False
    is_lower = False

    for ch in p:
        if ch.isdigit():
            is_num = True
        if ch.isupper():
            is_upper = True
        if ch.islower():
            is_lower = True

    if is_num and is_upper and is_lower:
        return "모든 조건 만족"
    else:
        return "하나씩 포함 해야함"
input_p = input("패스워드 입력 8자 :") 
msg = checkPass(input_p)
print(msg)