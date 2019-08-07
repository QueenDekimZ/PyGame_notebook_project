# @Time    : 2019/4/10 13:26
# @Author  : QueenDekimZ
# @Email   : QueenDekimZ@163.com
import pygame, sys
from math import pi

pygame.init()
screen  = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame图形绘制")
GOLD = 255, 251, 0
RED = pygame.Color("red")
WHITE = 255, 255, 255
GREEN = pygame.Color("green")

#r1rect = pygame.draw.rect(screen, GOLD, (200,100,200,100), 5)
#r2rect = pygame.draw.rect(screen, RED, (210,210,200,100), 0)

e1rect = pygame.draw.ellipse(screen, GREEN, (50, 50, 500, 300), 3)
c1rect = pygame.draw.circle(screen, GOLD, (200, 180), 30, 5)
c2rect = pygame.draw.circle(screen, GOLD, (400, 180), 30)
r1rect = pygame.draw.rect(screen, RED, (170, 130, 60, 10), 3)
r2rect = pygame.draw.rect(screen, RED, (370, 130, 60, 10))
plist = [(295,170),(285,250),(260,280),(340,280),(315,250),(305,170)]
l1rect = pygame.draw.lines(screen, GOLD, True, plist, 2)
a1rect = pygame.draw.arc(screen, RED, (200,220,200,100), 1.4*pi, 1.9*pi, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.update()