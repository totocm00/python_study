import random

sentences = [
    ["나는","학교","간다"],
    ["고양이가","창밖","본다"],
    ["오늘은","날씨","좋다"],
    ["엄마가","밥","했다"],
    ["친구와","게임","한다"],
    ["책을","많이","읽자"],
    ["아빠가","시장","간다"]
]

correct_count = 0

for i in range(1,6):
    print(f"\n문제 {i}:")
    
    answer_words = random.choice(sentences)
    shuffled_words = random.sample(answer_words,len(answer_words))

    print("다음의 단어들을 올바른 순서로 조합하세요: ")
    #print(" ".join(shuffle_words))
    print(shuffled_words)

    user_input = input("정확한 문장을 입력하세요 : ")

    answer_sentence = " ".join(answer_words)
    if user_input ==answer_sentence:
        print("정답입니다!")
        correct_count +=1
    else:
        print(f"틀렸습니다. 정답은 '{answer_sentence}'입니다")
print(f"\n{i}문제 중 {correct_count}개 맞췄습니다!")