import random
import time

msg1 = "네모난 침대에서 일어나 눈을 떠 보면"
msg2 = "네모난 창문으로 보이는 똑같은 풍경"
msg3 = "네모난 문을 열고 네모난 테이블에 앉아"
msg4 = "네모난 조간신문 본 뒤"
msg5 = "네모난 책가방에 네모난 책들을 넣고 네모난 버스를 타고"
msg6 = "네모난 건물 지나 네모난 학교에 들어서면 또"
msg7 = "네모난 교실 네모난 칠판과 책상들 네모난 오디오"
msg8 = "네모난 컴퓨터 TV 네모난 달력에 그려진 똑같은 하루를"
msg9 = "의식도 못한 채로 그냥 숨만 쉬고 있는걸"
msg10 = "주위를 둘러보면 모두 네모난 것들뿐인데"

msg_list = []
for i in range(1,11):
    msg_list.append(globals()["msg" + str(i)])

random_msg = random.choice(msg_list)

print(random_msg)

start_t = time.time()
typed = input("\n입력: ")

correct = 0
for i in range(min(len(random_msg),len(typed))):
    if random_msg[i] == typed[i]:
        correct += 1

end_t = time.time()
use_time = end_t - start_t

accuracy = correct / len(random_msg) * 100
cpm = len(typed) / use_time * 60
wrong = len(random_msg) - correct

print(f"\n🟢 정확도: {accuracy:.2f}%")
print(f"⌛ 걸린 시간: {use_time:.2f}초")
print(f"⌨️ 분당 타자 수 (CPM): {cpm:.2f}")
print(f"❌ 틀린 글자 수: {wrong}")