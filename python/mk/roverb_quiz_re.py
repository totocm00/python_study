score=0
idiom = [
    ["가까운","무당보다 먼 데 무당이 영하다"],
    ["긁어","부스럼"],
    ["경점 치고","문지른다"],
    ["꼬리가 길면","밟힌다"],
    ["내 일 바빠","한댁 방아"],
    ["망건 골에","앉았다"],
    ["석류는 떨어져도 안 떨어지는","유자를 부러워하지 않는다"],
    ["호박 덩굴이","벋을 적 같아서야"],
    ["이 열 번 물어도","모르면 송구하다"],
    ["죽 쑤고","개가 웃는다"],
    ["호랑이의 새끼를","만들지 않는다"]
]


for total in range(5):

	ran_list = random.choice(idiom)
	front = ran_list[0]
	back = ran_list[1]


	print(f"속담: \"{front}__\"")
	answer=input("뒤 답을 작성하시오").strip()
	
	if back == answer:
		print("정답입니다!\n")
		score +=1
	else:
		print(f"오답입니다. 힌트 \"{back[0]}\"")
		answer=input("뒤 답을 작성하시오").strip()

		if answer == back:
			print("정답입니다!")
		else:
			print(f"땡 정답: {back}")

	print("--------------------")
print(f"총 {total}중 {score}맞췄음")