import sys
time1 = float(input("시간을 입력하세요 : "))
if time1 < 0:
    print("양수로 입력하세요")
    sys.exit()
time2 = float(input("분을 입력하세요 : "))
if (time2 > 59):
    print("00~59 사이의 숫자를 입력하세요")
    sys.exit()
if (time2 < 0):
    print("양수로 입력하세요")
    sys.exit()
timeH = time1 * 60 * 60
timeM = time2 * 60
print("입력한 시간/분을 초로 변환한 값은 %d입니다." % (timeH + timeM))