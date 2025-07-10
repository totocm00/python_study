# 7
def mon_re():
    month_input = int(input("월을 입력하시오(1부터 12사이의 값) : "))
    return month_input
def day_re():    
    day_input = int(input("일을 입력하시오(1부터 31사이의 값) : "))
    return day_input

def getIntRange(a,b,msg):
    print(msg)
    mon_count = 0    
    day_count = 0    
    while not (1 <= a <= 12):
        print("월 다시 입력")
        a = mon_re()
        if (1 <= a <= 12):
            break
        mon_count += 1
    while not (1 <= b <= 31):
        print("일 다시 입력")
        b = day_re()
        if (1 <= b <= 31):
            break
        day_count += 1

    msg = "탈출을 축하 합니다"
    mon_day = f"{a}월{b}일"
    result = [a,b,msg,mon_day,mon_count,day_count]          
    return result

a = mon_re()
b = day_re()
msg = "정확한 수를 입력해야 탈출 가능"
getMonDay = getIntRange(a,b,msg)
print(getMonDay[3])