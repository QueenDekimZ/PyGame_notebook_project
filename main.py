# @Time    : 2019/4/9 12:32
# @Author  : QueenDekimZ
# @Email   : QueenDekimZ@163.com
import sys
import pygame
def main():
    pygame.init()   #初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行
    screen = pygame.display.set_mode((1200,900))   #创建屏幕对象（也即窗口对象）,分辨率1200*900
    pygame.display.set_caption("俄罗斯方块")   #窗口标题
    bg_color = (230,230,230)  #屏幕背景色
    while True:      #游戏主循环
        for event in pygame.event.get():  #监视键盘和鼠标事件
            if event.type == pygame.QUIT:  #关闭窗口的事件
                sys.exit()  #退出程序
        screen.fill(bg_color)  #填充屏幕背景色
        pygame.display.flip()  #刷新屏幕

if __name__ == '__main__':
    main()
