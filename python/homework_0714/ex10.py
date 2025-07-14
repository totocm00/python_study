# 10
def print_sym_dif(set1, set2):
    return print(set1.symmetric_difference(set2))
set1 = {x*10 for x in range(1,7)}
set2 = {x*10 for x in range(3,9)}

print_sym_dif(set1,set2)