import numpy as np
from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *
import cv2
import copy
import math

pi = 3.14
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
# 游戏状态
ANIMATION = 0
RUNNING = 1
GAMEOVER = 2

pygame.init()
pygame.display.set_caption("Flappy Big Ice")
# 设置游戏对话框尺寸
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 取背景图，抠掉边缘转换
background_day = pygame.image.load('flappybird/bg_day.png').convert_alpha()

bird = [pygame.image.load('assets/sprites/redbird-upflap.png').convert_alpha(),
		pygame.image.load('assets/sprites/redbird-midflap.png').convert_alpha(),
		pygame.image.load('assets/sprites/redbird-downflap.png').convert_alpha()]

number = [pygame.image.load('assets/sprites/0.png').convert_alpha(),
		  pygame.image.load('assets/sprites/1.png').convert_alpha(),
		  pygame.image.load('assets/sprites/2.png').convert_alpha(),
      	  pygame.image.load('assets/sprites/3.png').convert_alpha(),
		  pygame.image.load('assets/sprites/4.png').convert_alpha(),
	      pygame.image.load('assets/sprites/5.png').convert_alpha(),
	      pygame.image.load('assets/sprites/6.png').convert_alpha(),
		  pygame.image.load('assets/sprites/7.png').convert_alpha(),
		  pygame.image.load('assets/sprites/8.png').convert_alpha(),
		  pygame.image.load('assets/sprites/9.png').convert_alpha()]
# 地面图
ground = pygame.image.load('assets/sprites/base.png').convert_alpha()
# 开场动画
message = pygame.image.load('flappybird/text_ready.png').convert_alpha()
# 取柱子
pipe_down = pygame.image.load('flappybird/pipe_up.png').convert_alpha()
pipe_up = pygame.image.load('flappybird/pipe_down.png').convert_alpha()
# 取logo
logo = pygame.image.load('flappybird/bird0_0.png').convert_alpha()
# 取声音
if "win" in sys.platform:
    soundExt = '.wav'
else:
    soundExt = 'ogg'


sound_wing 	= pygame.mixer.Sound('assets/audio/wing'+soundExt)
sound_hit 	= pygame.mixer.Sound('assets/audio/hit'+soundExt)
sound_point = pygame.mixer.Sound('assets/audio/point'+soundExt)
sound_die 	= pygame.mixer.Sound('assets/audio/die'+soundExt)

# 取game over文本
text_game_over = pygame.image.load('flappybird/text_game_over.png').convert_alpha()

def showScore(score):
    # 拆分数字
    scoreDigits = [int(x) for x in list(str(score))]
    # 计算数字总宽度
    totalWidth = 0
    for digit in scoreDigits:
        totalWidth += number[digit].get_width()
    # 居中摆放
    score_x_position = (SCREEN_WIDTH - totalWidth) / 2
    score_y_position = int(0.2 * SCREEN_HEIGHT)
    # 刷新图
    for digit in scoreDigits:
        SCREEN.blit(number[digit], (score_x_position, score_y_position))
        score_x_position += number[digit].get_width()

def main():

    # 创建帧率实例
    FPS = pygame.time.Clock()
    # 迭代器 小鸟翅膀 0-1-2-1-0循环
    wing_position_iter = cycle([0,1,2,1])
    wing_position = 0
    # 迭代器 小鸟上下抖动
    bird_shake_iter = cycle([0,1,2,3,4,3,2,1,0,-1,-2,-3,-4,-3,-2,-1])
    bird_shake = 0

    bird_position = int(0.5 * SCREEN_HEIGHT)   # 小鸟起始高度
    bird_x_position = int(0.2 * SCREEN_WIDTH)   #小鸟水平位置
    ground_position = int(0.8 * SCREEN_HEIGHT - bird[0].get_height())   # 地面高度

    fps_count = 0  # 帧数处理
    key_down = 0  # 按键按下
    gravity = 1  # 重力大小
    down_velocity = 0  # 下降速度
    head_direction = 0  # 鸟头方向
    game_state = ANIMATION  # 游戏状态
    pipe_move_distance = SCREEN_WIDTH * 4 // 3 + pipe_down.get_width()  # 管子需要移动的距离
    pipe_gap = 30  # 管空隙大小
    pipe2_gap = 30  # 管2空隙大小
    pipe_x_position = SCREEN_WIDTH  # 柱子水平位置
    pipe_down_position = 0  # 下柱子管口位置
    pipe2_x_position = pipe_move_distance  # 柱子水平位置
    pipe2_up_position = 0
    pipe2_down_position = 0  # 下柱子管口位置
    score = 0  # 得分
    ground_x_position = 0  # 地面水平位置
    bird_actual_position = 0  # 小鸟实际高度
    # fisrt_fly_no_pipe 	= 90 # 开始一段没有柱子
    # 重绘logo大小
    logo_resize = pygame.transform.scale(logo, (30, 30))
    # 设置左上角icon
    pygame.display.set_icon(logo_resize)

    while 1:
        # 获取鼠标按键状态
        for event in pygame.event.get():
            if  event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                if game_state == ANIMATION:
                    game_state = RUNNING
                    down_velocity = 0  # 下降速度
                    head_direction = 0  # 鸟头方向
                    fps_count = 0  # 帧数处理
                    score = 0  # 得分
                    pipe_x_position = SCREEN_WIDTH  # 柱子水平位置
                    pipe2_x_position = pipe_move_distance  # 柱子水平位置

                if game_state == RUNNING:
                    key_down = 6
                    sound_wing.play()
                if game_state == GAMEOVER:
                    # 小鸟落地后游戏才能重新开始
                    if bird_actual_position == ground_position:
                        game_state = ANIMATION
                        bird_position = int(0.5 * SCREEN_HEIGHT)  # 小鸟起始高度

        # 刷新背景
        SCREEN.blit(background_day, (0, 0))

        if game_state == ANIMATION:
            fps_count += 1
            SCREEN.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, 0.1 * SCREEN_HEIGHT))
            # 草地动起来
            ground_x_position = -1 * ((fps_count * 4) % (ground.get_width() - SCREEN_WIDTH))
            SCREEN.blit(ground, (ground_x_position, int(0.8 * SCREEN_HEIGHT)))
            # 更新翅膀位置，比帧数放慢4倍
            if fps_count % 4 == 0:
                wing_position = next(wing_position_iter)
            # 小鸟上下抖动
            bird_shake = next(bird_shake_iter)
            # 小鸟动起来
            bird_actual_position = bird_position + bird_shake
            SCREEN.blit(bird[wing_position], (bird_x_position, bird_actual_position))
        if game_state == RUNNING:
            # 帧数处理
            fps_count += 1
            # 游戏刚开始时候没有柱子空飞一段
            # if fps_count*4 > SCREEN_WIDTH+pipe_down.get_width():
            if 1:
                # 柱子动起来
                if pipe_x_position == SCREEN_WIDTH:
                    pipe_down_position = random.randrange(int(0.3 * SCREEN_HEIGHT), int(0.7 * SCREEN_HEIGHT), 10)
                    pipe_gap = random.randrange(100, 151, 10)
                pipe_up_position = pipe_down_position - pipe_gap - pipe_up.get_height()
                pipe_x_position = SCREEN_WIDTH - (fps_count * 4) % pipe_move_distance
                SCREEN.blit(pipe_down, (pipe_x_position, pipe_down_position))
                SCREEN.blit(pipe_up, (pipe_x_position, pipe_up_position))
            if fps_count * 4 > pipe_move_distance // 2:

                # 柱子2动起来
                if pipe2_x_position == pipe_move_distance:
                    pipe2_down_position = random.randrange(int(0.3 * SCREEN_HEIGHT), int(0.7 * SCREEN_HEIGHT), 10)
                    pipe2_gap = random.randrange(100, 151, 10)
                pipe2_up_position = pipe2_down_position - pipe2_gap - pipe_up.get_height()
                pipe2_x_position = pipe_move_distance - pipe_down.get_width() - (
                            fps_count * 4 - pipe_move_distance // 3) % pipe_move_distance
                SCREEN.blit(pipe_down, (pipe2_x_position, pipe2_down_position))
                SCREEN.blit(pipe_up, (pipe2_x_position, pipe2_up_position))

            # 草地动起来
            ground_x_position = -1 * ((fps_count * 4) % (ground.get_width() - SCREEN_WIDTH))
            SCREEN.blit(ground, (ground_x_position, int(0.8 * SCREEN_HEIGHT)))
            # 更新翅膀位置，比帧数放慢4倍
            if fps_count % 4 == 0:
                wing_position = next(wing_position_iter)
            # 小鸟上下抖动
            bird_shake = next(bird_shake_iter)
            # 小鸟受重力下落, 按键按下则上升
            if key_down:
                # 刷新的过程需要key_down递减之0 用几帧画面完成
                key_down -= 1
                bird_position -= 6
                bird_position = max(0, bird_position)  # 边界检测
                down_velocity = 0
                head_direction += 6
                head_direction = min(24, head_direction)  # 边界检测
            else:
                down_velocity += gravity
                bird_position += down_velocity
                bird_position = min(bird_position, ground_position)  # 边界检测
                head_direction -= 3
                head_direction = max(-42, head_direction)  # 边界检测

            # 调整头的方向
            bird_head = pygame.transform.rotate(bird[wing_position], head_direction)
            # 小鸟动起来
            bird_actual_position = bird_position + bird_shake
            SCREEN.blit(bird_head, (bird_x_position, bird_actual_position))
            # 检测撞地
            if bird_position == ground_position:
                game_state = GAMEOVER
                sound_hit.play()

            # 检测撞柱子
            # 小鸟水平位置在柱子管水平宽度内
            if bird_x_position + bird[0].get_width() > pipe_x_position and \
                    bird_x_position < pipe_x_position + pipe_down.get_width():
                # 小鸟高度比下管道低或比上管道高
                if bird_actual_position + bird[0].get_height() > pipe_down_position or \
                        bird_actual_position < pipe_down_position - pipe_gap:
                    game_state = GAMEOVER
                    sound_hit.play()
                    sound_die.play()
            # 小鸟水平位置在柱子2管水平宽度内
            if bird_x_position + bird[0].get_width() > pipe2_x_position and \
                    bird_x_position < pipe2_x_position + pipe_down.get_width():
                # 小鸟高度比下管道低或比上管道高
                if bird_actual_position + bird[0].get_height() > pipe2_down_position or \
                        bird_actual_position < pipe2_down_position - pipe2_gap:
                    game_state = GAMEOVER
                    sound_hit.play()
                    sound_die.play()

            # 小鸟飞过管道后壁刷新得分
            if abs(bird_x_position - (pipe_x_position + pipe_down.get_width())) < 2 or \
                    abs(bird_x_position - (pipe2_x_position + pipe_down.get_width())) < 2:
                sound_point.play()
                score += 1
            showScore(score)

        if game_state == GAMEOVER:
            # 调整头的方向
            bird_head = pygame.transform.rotate(bird[wing_position], -90)
            SCREEN.blit(pipe_down, (pipe_x_position, pipe_down_position))
            SCREEN.blit(pipe_up, (pipe_x_position, pipe_up_position))
            SCREEN.blit(pipe_down, (pipe2_x_position, pipe2_down_position))
            SCREEN.blit(pipe_up, (pipe2_x_position, pipe2_up_position))
            SCREEN.blit(ground, (ground_x_position, int(0.8 * SCREEN_HEIGHT)))
            bird_actual_position += 10
            bird_actual_position = min(ground_position, bird_actual_position)
            SCREEN.blit(bird_head, (bird_x_position, bird_actual_position))
            showScore(score)
            # 小鸟落地后游戏才能重新开始
            if bird_actual_position == ground_position:
                SCREEN.blit(text_game_over, (SCREEN_WIDTH / 2 - text_game_over.get_width() / 2, 0.4 * SCREEN_HEIGHT))
        # 设置文中logo
        SCREEN.blit(pygame.image.load('flappybird/white.png').convert_alpha(),
                    (SCREEN_WIDTH / 2 - 20 , SCREEN_HEIGHT - 70))
        # 图片刷新
        pygame.display.update()
        # 设置帧率30帧
        FPS.tick(30)


if __name__ == "__main__":
    main()

