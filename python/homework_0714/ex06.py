# 6
list_key = [1,2,3,4,5]
list_value = ["노래","코딩","뿌뿌뿌","쿠아앙","우왕"]
list_dic = {}
list_dic = {key : val for key, val in zip(list_key, list_value)}
print(list_dic)

list_key = [1,2,3,4,5,6]
list_value = ["노비","코피","뿡","쿠아앙","우왕"]
list_dics = dict(zip(list_key, list_value))
print(list_dics)