# 5
def sum_price(my_dic):
    price = 0
    for key, value in my_dic.items():
        price += value
    return price

my_dic = {"옷":100, "컴퓨터":2000,"모니터":320}
price = sum_price(my_dic)
print(price)