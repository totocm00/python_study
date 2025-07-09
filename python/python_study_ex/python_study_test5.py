R , r = 'R' , 'r'
T , t = 'T' , 't'
C , c = 'C' , 'c'
x4 = input("하나의 문자를 입력하세요 : ")
core = ""
if (x4 == R or x4 == r):
    core = "Rectangle"
if (x4 == T or x4 == t):
    core = "Triangle"
if (x4 == C or x4 == c):
    core = "Circle"

if (core != ""):
    print(core)
else:
    print("Unknown")

print("끝")