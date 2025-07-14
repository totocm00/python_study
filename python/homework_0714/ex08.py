# 8
def print_choice_moon_nam(user_inp):
    for key, value in list_month_nam.items():
        if user_inp == key:
            print(f"{key} -> {value}")


list_month_nam = {1:"January", 2:"February", 3:"March", 4:"April",
                  5:"May", 6:"June", 7:"July", 8:"August", 9: "September",
                  10:"October", 11:"Novermber", 12:"December"}

user_inp = int(input("원하는 달의 숫자를 입력: "))
print_choice_moon_nam(user_inp)