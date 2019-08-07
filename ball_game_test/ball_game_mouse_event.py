# @Time    : 2019/4/10 10:00
# @Author  : QueenDekimZ
# @Email   : QueenDekimZ@163.com
import sys
import pygame
def main():
    #bg_size = width, height = 1000, 660
    pygame.init()   #初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行
    #vInfo= pygame.display.Info()
    bg_size = width, height = 900, 600
    bg_color = (230, 230, 230)  # 屏幕背景色
    speed = [1, 1]

    #bg_size = width, height = vInfo.current_w, vInfo.current_h
    #print(width,height)
    #screen = pygame.display.set_mode(bg_size, pygame.FULLSCREEN)   #创建屏幕对象（也即窗口对象）,分辨率1200*900
    screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)
    #set_mode(r=(0,0),flags=0) flags用来显示类型，可用|组合使用
    #常用pygame.RESIZABLE 窗口大小可调用   #要有尺寸变化的响应
    #pygame.NOFRAME 窗口没有边界显示    #增加退出方式
    #pygame.FULLSCREEN 窗口全屏显示    #分辨率对应问题

    pygame.display.set_caption("Python壁球")   #窗口标题
    # display.set_caption(title,icontitle=None)
    # display.get_caption() 反回元组(title,icontitle) 该函数与游戏交互逻辑配合，可以根据游戏情节修改标题内容
    # display.set_icon(surface) 设置窗口的图标效果 图标是一个Surface对象

    ball = pygame.image.load('../image/PYG02-ball.gif')
    icon = pygame.image.load('../image/PYG03-flower.png')

    pygame.display.set_icon(icon)
    ballrect = ball.get_rect()

    fps = 20000
    still = False
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    still = True
            elif event.type == pygame.MOUSEBUTTONUP:
                still = False
                if event.button == 1:
                    ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:
                    ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)



            elif event.type == pygame.VIDEORESIZE:
                bg_size = width, height = event.size[0], event.size[1]
                screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)
            #pygame.event.EventType  封装的数据类型（对象），Pygame的一个类，表示事件类型
                                    # 事件类型只有属性没有方法
                                    # 用户可以自定义新的事件类型

        if pygame.display.get_active() and not still:
            ballrect = ballrect.move(speed[0], speed[1])
        # display.get_active() 窗口在系统中显示（屏幕绘制/非图标化）时返回True，否则返回False
        # 判断窗口是否被最小化  进一步可以暂停游戏，改变响应模式等

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
            if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
                speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
            if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
                speed[1] = -speed[1]
        screen.fill(bg_color)  #填充屏幕背景色
        screen.blit(ball, ballrect)
        pygame.display.update()  #刷新屏幕，变化的部分
        #pygame.display.flip()  刷新整个窗口
        fclock.tick(fps)   #控制帧速度，即窗口刷新速度，每秒最大framerate次帧刷新
if __name__ == '__main__':
    main()

