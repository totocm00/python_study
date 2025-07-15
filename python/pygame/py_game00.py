import pygame

#초기화 ---------------init구간
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 버퍼
pygame.display.set_caption("PY게임!") # 맨 위의 타이틀 바

# screen.fill((0,0,0)) # RGB -> 출력하라는 로직 / 그래서 한 번 보여주고 끝

# ---------------------------

while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        # KEYDOWN 이벤트 -> 눌렀을 때 실행
        # KEYUP 이벤트 -> 뗏을 때 실행
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()