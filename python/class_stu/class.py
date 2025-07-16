class Car:
    clolor = ""
    speed = 0
    def __init__(self):
        self.clolor = ""
        self.speed = 30
    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.downSpeed -= value
    #추가된 메서드
    def printMessage(self) :
        print("시험 출력이다.")

car1 = Car()
car1.upSpeed(30)
print(car1.speed)

car1.upSpeed(30)
print(car1.speed)
