import random

list_a = [["나는", "학교를", "간다"], ["나는", "늦게", "달린다"],["오늘","학교를","쨋다"],["나는","학원을","쨋다"]]

def random_choice():
    return random.choice(list_a)

def print_mix_list(sentence):
    mixed = sentence.copy()
    random.shuffle(mixed)
    print("섞인 단어:", mixed)
    return mixed

def user_input_list():
    return input("입력하세요: ").split()

answer = 0
stage_nums = 5
for stage in range(stage_nums):

    correct_list = random_choice()
    print(f"\n문제 {stage + 1}:")
    print_mix_list(correct_list)

    user_input = user_input_list()
    temp = []

    for i in range(min(len(correct_list), len(user_input))):
        if user_input[i] == correct_list[i]:
            temp.append(user_input[i])
        else:
            if i == min((len(correct_list), len(user_input))):
                break
    

    if user_input == correct_list:
        print("정답")
        answer += 1
    else:
        print("실패")
        if temp:
            print("맞춘 단어:"," ".join(temp))
        else:
            print("한문제도 못 맞춤")
        print("정답은:", " ".join(correct_list))

print(f"맞춘 수: {answer}")
print("Su go!")