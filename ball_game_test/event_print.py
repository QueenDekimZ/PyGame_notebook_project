# @Time    : 2019/4/9 20:57
# @Author  : QueenDekimZ
# @Email   : QueenDekimZ@163.com
import pygame, sys

pygame.init()
screen  = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame事件处理")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]", "#", event.key, event.mod)
            else:
                print("[KEYDOWN]", event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            print("【MOUSEBUTTONMOTION]:",event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("【MOUSEBUTTONDOWN]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("【MOUSEBUTTONUP]:", event.pos, event.button)
    pygame.display.update()


#pygame.event.MOUSEMOTION 鼠标移动事件
#   event.pos 鼠标当前坐标值(x,y)，相对于窗口左上角
#   event.rel 鼠标相对运动距离(X,Y)，相对于上次事件
#   event.buttons 鼠标按钮状态(a,b,c)，对应于鼠标的三个键  鼠标移动时，这三个键处于按下状态，对应位置为1，反之则为0
#pygame.event.MOUSEBUTTONUP 鼠标释放事件
#   event.pos 鼠标当前坐标值(x,y)，相对于窗口左上角
#   event.button 鼠标按下键编号n，取值1/2/3，分别对应三个键
#pygame.event.MOUSEBUTTONDOWN 鼠标键按下事件
#    event.pos 鼠标当前坐标值(x,y)，相对于窗口左上角
#    event.button 鼠标按下键编号n，取值为整数，左键为1，右键为3，设备相关
#
#