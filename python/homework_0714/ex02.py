# x : x*x 형식의 숫자 (1과 10사이)
square_dict = {x: x**2 for x in range(1, 11)}
print(square_dict)

square = lambda x: x**2
square_dict = {x: square(x) for x in range(1, 11)}
print(square_dict)