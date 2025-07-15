import pygame

#초기화
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 버퍼
pygame.display.set_caption("PY게임!") # 맨 위의 타이틀 바

screen.fill((0,0,0)) # RGB