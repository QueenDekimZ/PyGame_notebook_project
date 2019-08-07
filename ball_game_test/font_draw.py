# @Time    : 2019/4/10 18.41
# @Author  : QueenDekimZ
# @Email   : QueenDekimZ@163.com
import pygame, sys
import pygame.freetype

pygame.init()
screen  = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame文字绘制")

GOLD = 255, 251, 0

f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1surf, f1rect = f1.render("世界和平", fgcolor=GOLD, size=50)
#f1rect = f1.render_to(screen, (200,160), "世界和平", fgcolor=GOLD, size=50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(f1surf, (100,50))
    pygame.display.update()

    ######################################################################
    # pygame.freetype 向屏幕上绘制特定字体的文字
    # 文字不能直接print(),而是用像素根据字体点阵图绘制
    # pygame.freetype.Font(file, size=0)
    #                     字体类型名称或路径 字体大小

    #   Font类绘制方法（1）
    #   Font.render_to(surf,dest,text,fgcolor=None,bgcolor=None,rotation=0,size=0) ->Rect
    #   surf 绘制字体的平面，Surface对象
    #   dest 在平面中的具体位置，（x,y）
    #   text 绘制的字体内容
    #   fgcolor 文字颜色
    #   bgcolor 背景颜色
    #   rotation 逆时针的旋转角度，取值0-359，部分字体可旋转
    #   size 文字大小，赋值该参数将覆盖Font中的设定值

    #   Font类的绘制方法（2）
    #   Font.render(text, fgcolor=None, bgcolor=None, rotation=0, size=0) ->(Surface, Rect)