class Card:
    kind = ""
    number = 0
    width = 100 # 클래스 변수
    height = 250 # 클래스 변수

# 매개변수가 있는 생성자
    def __init__(self,kind, number):
        self.kind = kind
        self.number = number


    def __str__(self):
        print("kind : ", self.kind)
        print("number : ",self.number)
        print("width : ", Card.width)
        print("height : ", Card.height)
        print("아래는 msg 리턴 내용")

        return f"kind:{self.kind}\n number:{self.number}\n width:{Card.width}\n height:{Card.height}"



if __name__ == "__main__":
    card1 = Card("다이아몬드", 10)
    card1.__str__()
    print()
    print(card1)

    print()
    card2 = Card("스페이드", 11)
    card2.__str__()

