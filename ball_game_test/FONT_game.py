# @Time    : 2019/4/10 20:13
# @Author  : QueenDekimZ
# @Email   : QueenDekimZ@163.com
import sys
import pygame
import pygame.freetype
def main():
    #bg_size = width, height = 1000, 660
    pygame.init()   #初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行
    #vInfo= pygame.display.Info()
    bg_size = width, height = 900, 600
    bg_color = (230, 230, 230)  # 屏幕背景色
    GOLD = 255, 251, 0

    pos = [230,160]
    speed = [1, 1]

    screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)

    pygame.display.set_caption("Python动态文字")   #窗口标题
    icon = pygame.image.load('../image/PYG03-flower.png')

    f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
    f1rect = f1.render_to(screen, pos, "世界和平", fgcolor=pygame.Color("black"), size=50)

    pygame.display.set_icon(icon)
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

        if pos[0] < 0 or pos[0] + f1rect.width > width:
            speed[0] = -speed[0]
        if pos[1] < 0 or pos[1] + f1rect.height > height:
            speed[1] = -speed[1]
        pos[0] = pos[0] + speed[0]
        pos[1] = pos[1] + speed[1]
        screen.fill(bg_color)  #填充屏幕背景色
        if pygame.display.get_active():
            f1rect = f1.render_to(screen, pos, "世界和平", fgcolor=pygame.Color("black"), size=50)
S
        pygame.display.update()  # 刷新屏幕，变化的部分
        #screen.blit(f1surf, (pos[0], pos[1]))
        fclock.tick(fps)   #控制帧速度，即窗口刷新速度，每秒最大framerate次帧刷新
if __name__ == '__main__':
    main()
