import pygame

#초기화 ---------------init구간
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 버퍼
pygame.display.set_caption("PY게임!") # 맨 위의 타이틀 바

clock = pygame.time.Clock() # clock을 정의. pygame 안에 time 함수 있음

# screen.fill((0,0,0)) # RGB -> 출력하라는 로직 / 그래서 한 번 보여주고 끝

# 폰트 지정 / 맑은 고딕
FONT = pygame.font.SysFont("malgun gothic", 48)
# render -> 화면에 쓰기위한 함수
text = FONT.render("Intel", True, (255,255,255))

# 이미지를 추가하는 방법
img = pygame.image.load(r"C:\Users\types\OneDrive\Desktop\피카츄.jpg")
# 이미지의 크기가 크면 스케일 다운을 해줌 
img = pygame.transform.scale(img, (300, 300)) 

# 좌표 설정
x = 250
y = 150

# ---------------------------

while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        # KEYDOWN 이벤트 -> 눌렀을 때 실행
        # KEYUP 이벤트 -> 뗏을 때 실행
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    
    # 이미지 표시
    screen.blit(img, (x, y))

    # 텍스트 표시
    # block transfer
    # : 한 이미지의 픽셀 데이터를 다른 표면(Surface)으로 복사하는 작업
    screen.blit(text, (330,0))
    
    # display에 내용을 업데이트 시킴
    pygame.display.update()

    y += 1
    if y > 600:
        y = 0
    screen.blit(text, (x,y))
    pygame.display.update()
            
    clock.tick(60)   # FPS 개념이 .tick = 즉, (숫자)의 FPS
