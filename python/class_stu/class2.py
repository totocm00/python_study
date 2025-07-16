class Car:
	color = ""
	speed = 0
	count = 0
	## 매개변수 있는 생성자
	def __init__(self, color, speed):
		self.color = color
		self.speed = speed
		Car.count += 1
		
		
	def upSpeed(self, value) :
		self.speed += value
		
	def downSpeed(self, value) :
		self.speed -= value
		
	def printMessage(self):
		print(f"{self.color} {self.speed} {Car.count}")

myCar1 = Car("빨강",50)
myCar2 = Car("노랑",100)
myCar3 = Car("파랑",150)

myCar3.printMessage()