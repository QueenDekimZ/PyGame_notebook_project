# @Time    : 2019/4/9 13:28
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
            #pygame.event.EventType  封装的数据类型（对象），Pygame的一个类，表示事件类型
                                    # 事件类型只有属性没有方法
                                    # 用户可以自定义新的事件类型
        if pygame.display.get_active():
            ballrect = ballrect.move(speed[0], speed[1])
        # display.get_active() 窗口在系统中显示（屏幕绘制/非图标化）时返回True，否则返回False
        # 判断窗口是否被最小化  进一步可以暂停游戏，改变响应模式等

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        screen.fill(bg_color)  #填充屏幕背景色
        screen.blit(ball, ballrect)
        pygame.display.update()  #刷新屏幕，变化的部分
        #pygame.display.flip()  刷新整个窗口
        fclock.tick(fps)   #控制帧速度，即窗口刷新速度，每秒最大framerate次帧刷新
if __name__ == '__main__':
    main()


# pygame.event.KEYDOWN      event.unicode 对应键unicode编码   # unicode码与平台有关，不推荐使用
#                           event.key  对应键的常量名称
#                           event.mod  键盘按下时键盘提供的状态模式，按键修饰符的组合值
                            #修饰符的按位或运算 event.mod = KMOD_ALT | KMOD_SHIFT
#处理事件         event.get() poll() clear()
#操作事件队列      event.set_blocked() get_blocked() set_allowed()
#生成事件          event.post() Event()

#event.get(type) event.get(typelist) 从事件队列中获得事件列表，即获得所有被队列的事件
#            增加参数，获得某类或某些类事件

#event.poll() 从事件队列中获得一个事件   事件获取将从事件队列中删除
#             如果事件队列为空，则返回 event.NOEVENT

#event.clear(type) event.clear(typelist)   从事件队列中删除事件，默认删除所有事件
#                该函数与event.get()类似，区别仅是不对事件进行处理
#                可以增加参数，删除某类或某些类事件


###################   事件队列最多同时存储128个事件 #######################
#队列满时，更多事件将被丢弃
# 操作事件队列      event.set_blocked() get_blocked() set_allowed()
# 设置事件队列能够储存事件的类型
# set_blocked(type or typelist)  控制哪些类型事件不允许被保存到事件队列中
# get_blocked(type or typelist)  允许
# set_allowed(type)  测试事件类型，被禁止返回True，否则返回False

# event.post(Event)
# 产生一个事件，并将其放入事件队列
#一般用于放置用户自定义事件（pygame.USEREVENT)
#也可以用于放置系统定义事件（如鼠标和键盘等），给定参数
# event.Event(type, dict)
# 创建一个给定类型的事件
# 其中，事件的属性和值采用字典类型复制，属性名采用字符串形式
# 如果创建已有事件，属性需要一致

########################################################################
#pygame.Color
# RGB或RGBA，A可选
# Color类可以用色彩名字，RGBA值，HTML色彩格式等方式定义
# Color(name)          Color("grey")
# Color(r,g,b,a)       Color(190,190,190,255)
# Color(rgbvalue)      Color("BEBEBEFF")      十六进制
# Color.normalize  归一化

#######################################################################
# pygame.draw.rect(Surface, color, Rect, width=0)
#                      screen     (x,y,w,h)
# pygame.draw.polygon(Surface, color, pointlist, width=0)
#                                     多边形顶点坐标列表   边缘宽度，即填充图形
#pygame.draw.circle(Surface, color, pos, radius, width=0)
#                                  圆心坐标 半径
#pygame.draw.ellipse(Surface, color, Rect width=0) 椭圆形
#pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=0)
#                               椭圆形绘制区域 起始和结束弧度值 横向右侧为0度
#pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
#                                直线的起始和结束坐标
#pygame.draw.lines(Surface, color, closed, pointlist, width=1)
#                                 如果为True,起止节点间自动增加封闭直线 连续多线的顶点坐标列表
#pygame.draw.aaline(Surface,color,start_pos,end_pos,blend=1)
#                                    blend不为0时，与线条所在背景颜色进行混合
#pygame.draw.aalines(Surface, color, closed, pointlist, blend-1)

######################################################################
# pygame.freetype 向屏幕上绘制特定字体的文字
# 文字不能直接print(),而是用像素根据字体点阵图绘制
#pygame.freetype.Font(file, size=0)
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

# Surface 主图层  display.set_mode()生成
# 主图层上绘制其他图层使用.blit()方法
# screen.blit(Surface, Rect)