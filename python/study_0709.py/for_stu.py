fruits = ["apple", "banan", "orange", "grape", "kiwi"]
search_fruit = "orange"

for fruit in fruits:
    if fruit == search_fruit:
        print(f"찾는 과일 '{search_fruit}' 을(를) 찾았습니다! ")
        break # "orange" 를 찾았으니 루프를 즉시 종료
    print(f"현재 확인 중인 과일: {fruit}")
print("탐색을 완료했습니다")