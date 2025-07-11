import qrcode
import random

def generate_qr_from_text(text):
    return qrcode.make(text)

# 초기 속담 리스트
proverbs = [
    ["굴러온 돌이", "박힌 돌 뺀다"],
    ["긁어", "부스럼"],
    ["돼지에", "진주 목걸이"],
    ["꼬리가 길면", "밟힌다"],
    ["돌다리도", "두들겨 보고 건너라"],
    ["마른하늘에", "날벼락"]
]

questions = []
correct_answers = []
user_inputs = []

while proverbs:  # 속담이 남아 있는 동안 반복
    proverb = random.choice(proverbs)
    front, back = proverb

    print(f"\n문제: {front}")

    first_input = input("첫 번째 답: ").strip()

    if first_input == back:
        user_inputs.append(f"첫 번째 답: {first_input}")
    else:
        # 힌트 제공
        hint = back[0]
        print(f"힌트: {hint}...")
        second_input = input("두 번째 답: ").strip()

        if second_input == back:
            user_inputs.append(f"첫 번째 답: {first_input}\n두 번째 답: {second_input}")
        else:
            user_inputs.append(f"첫 번째 답: {first_input}")

    questions.append(front)
    correct_answers.append(back)
    proverbs.remove(proverb)  # 출제된 속담 제거

    if not proverbs:
        print("\n모든 문제를 푸셨습니다. 게임이 종료됩니다.")
        break

    choice = input("계속 하시겠습니까? (y/n): ").strip().lower()
    match choice:
        case "y":
            continue
        case "n":
            print("게임을 종료합니다.")
            break
        case _:
            print("잘못된 입력입니다. 자동 종료합니다.")
            break

# QR 텍스트 생성
combined_text = ""
for i in range(len(questions)):
    combined_text += f"{i+1}번 문제: {questions[i]}\n"
    combined_text += f"{user_inputs[i]}\n"
    combined_text += f"정답: {correct_answers[i]}\n\n"

final_qr = generate_qr_from_text(combined_text)
print("\n=== 결과 QR코드 생성 완료! 스캔해서 확인하세요 ===")
final_qr.show()