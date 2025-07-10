#1번 2 * 3.14 * r   ridius 반지름
# form math import pi
# 모듈은 math 인데 pi를 import 할거라는 의미
# 모듈 지정해서 가지고 올 때
# 위를 안하면 math.pi 라고 계속 해줘야함
# 3.14 == pi
def get_perl(radius):
    radius = 5
    return print(2*3.14*radius)
get_perl(3)