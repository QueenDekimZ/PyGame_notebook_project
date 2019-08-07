# @Time    : 2019/4/9 13:28
# @Author  : QueenDekimZ
# @Email   : QueenDekimZ@163.com
import sys
import pygame
def main():
    #bg_size = width, height = 1000, 660
    pygame.init()   #初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行
    vInfo = pygame.display.Info()
    bg_size = width, height = vInfo.current_w, vInfo.current_h
    #print(width,height)
    screen = pygame.display.set_mode(bg_size, pygame.FULLSCREEN)   #创建屏幕对象（也即窗口对象）,分辨率1200*900
    #print(bg_size)
    #set_mode(r=(0,0),flags=0) flags用来显示类型，可用|组合使用
    #常用pygame.RESIZABLE 窗口大小可调用   #要有尺寸变化的响应
    #pygame.NOFRAME 窗口没有边界显示    #增加退出方式
    #pygame.FULLSCREEN 窗口全屏显示    #分辨率对应问题


    speed = [1, 1]
    pygame.display.set_caption("Python壁球")   #窗口标题
    bg_color = (230,230,230)  #屏幕背景色
    ball = pygame.image.load('../image/PYG03-flower.png')
    ballrect = ball.get_rect()
    fps = 20000
    fclock = pygame.time.Clock()
    while True:      #游戏主循环
        for event in pygame.event.get():  #监视键盘和鼠标事件
            if event.type == pygame.QUIT:  #关闭窗口的事件
                sys.exit()  #退出程序
            elif event.type == pygame.KEYDOWN: #键盘敲击事件 K_UP or K_DOWN or K_LEFT or K_RIGHT
                if event.key == pygame.K_LEFT:
                    speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)*int(speed[0]/abs(speed[0]))
                elif event.key == pygame.K_RIGHT:
                    speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
                elif event.key == pygame.K_DOWN:
                    speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1)*int(speed[1]/abs(speed[1]))
                elif event.key == pygame.K_UP:
                    speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                bg_size = width, height = event.size[0], event.size[1]
                screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)
        ballrect = ballrect.move(speed[0], speed[1])
        #print(abs(ballrect.right - ballrect.left))
        #print(abs(ballrect.top - ballrect.bottom))
        if ballrect.left <= 0 or ballrect.right >= width:
            speed[0] = -speed[0]
        if ballrect.top <= 0 or ballrect.bottom >= height:
            speed[1] = -speed[1]
        screen.fill(bg_color)  #填充屏幕背景色
        screen.blit(ball, ballrect)
        pygame.display.update()  #刷新屏幕
        fclock.tick(fps)   #控制帧速度，即窗口刷新速度，每秒最大framerate次帧刷新
if __name__ == '__main__':
    main()
