d = {"apple":1, "banana":2, "grape":3}
def get_dicList(d):
    for key, num in d.items():
        print(key," -> ",num,end=" |")

get_dicList(d)