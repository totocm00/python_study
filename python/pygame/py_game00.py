import pygame

#초기화 ---------------init구간
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 버퍼
pygame.display.set_caption("PY게임!") # 맨 위의 타이틀 바

# screen.fill((0,0,0)) # RGB -> 출력하라는 로직 / 그래서 한 번 보여주고 끝

# 폰트 지정 / 맑은 고딕
FONT = pygame.font.SysFont("malgun gothic", 48)
# render -> 화면에 쓰기위한 함수
text = FONT.render("Intel", True, (255,255,255))
# ---------------------------

while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        # KEYDOWN 이벤트 -> 눌렀을 때 실행
        # KEYUP 이벤트 -> 뗏을 때 실행
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    
    # block transfer
    # : 한 이미지의 픽셀 데이터를 다른 표면(Surface)으로 복사하는 작업
    screen.blit(text, (330,0))
    # display에 내용을 업데이트 시킴
    pygame.display.update()
            