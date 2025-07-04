user_input = int(input("100000(십만) ~ 999999(99만9999) 사이의 숫자를 입력 : "))

if user_input>=100000 and user_input<1000000:
    moreT = user_input//1000
    lessT = user_input % 1000
    print(moreT,",",lessT)
    print(moreT + lessT)
    print(str(moreT)+","+str(lessT))
    print("%d,%d"% (moreT,lessT))
    print(f"{moreT},{lessT}")