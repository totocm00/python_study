# 7
def mon_re():
    month_input = int(input("월을 입력하시오(1부터 12사이의 값) : "))
    return month_input
def day_re():    
    day_input = int(input("일을 입력하시오(1부터 31사이의 값) : "))
    return day_input

def loop_input(star1,end1,inputS,msg,fun_re):
    count = 0
    while not (star1 <= inputS <= end1):
        print(msg)
        inputS = fun_re()
        if (star1 <= inputS <= end1):
            break
        count += 1
    return inputS,count

def getIntRange(a,b,msg):
    print(msg)  
    a, mon_count = loop_input(1, 12, a, "월 다시 입력", mon_re)
    b, day_count = loop_input(1, 31, b, "일 다시 입력", day_re)

    msg = "탈출을 축하 합니다"
    mon_day = f"{a}월{b}일"
    result = [a,b,msg,mon_day,mon_count,day_count]          
    return result

a = mon_re()
b = day_re()
msg = "정확한 수를 입력해야 탈출 가능"
getMonDay = getIntRange(a,b,msg)
print(getMonDay[3])