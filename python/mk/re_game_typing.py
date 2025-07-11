import random
import time

def loop_typed():
    typed = input("입력")
    return typed

def check_100(correct,over_minu,len_tar):
    accuracy = (correct-over_minu) / len_tar * 100
    return accuracy

def len_tar_len_type(target,typed,elapsed):
    correct = 0
    over_minu = 0
    len_tar = len(target)
    len_type = len(typed)

    if len_tar < len_type:
        over_minu = abs(len_tar - len_type)

    for i in range(min(len_tar,len_type)):
        if target[i] == typed[i]:
            correct +=1
    
    accuracy = check_100(correct,over_minu,len_tar)
    speed = (len_type-over_minu) / elapsed * 60

    return len_tar, len_type, accuracy, speed

sentences = [
    "시원한 아이스크림 들고서",
    "우리 같이 걸을래",
    "자전거로 한강에 갈래"
]
target = random.choice(sentences)
print(f"{target}")

start_time = time.time()
typed = loop_typed()

end_time = time.time()
elapsed = end_time - start_time

len_tar, len_type, accuracy, speed = len_tar_len_type(target,typed,elapsed)

while True:
    typed = loop_typed()
    end_time = time.time()
    elapsed = end_time - start_time

    break_point = False
    len_tar, len_type, accuracy, speed = len_tar_len_type(target, typed, elapsed)

    if accuracy == 100:
        break

print(accuracy)
print(speed)