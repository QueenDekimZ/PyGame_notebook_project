import random
# 画棋盘的函数，传入一个放置棋子的列表
def drawBoard(board):
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("------------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("------------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])


# 玩家选择所想用的棋子种类
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O")
        # 自动将小写转化为大写
        letter = input().upper()

    # 如果玩家选择的X，则自动将O赋给电脑，反之一样
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# 这里随机生成0或者1来表示谁先落子
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


# 如果玩家选择y或者Y则游戏重新开始
def playAgain():
    print("Do you want to play again?(yes or no)")
    return input().lower().startswith('y')


# 将棋子放置到棋盘上面
# board参数是储存棋子的列表
# letter参数是棋子的类型
# move是选择将棋子放在哪
def makeMove(board, letter, move):
    board[move] = letter


#  根据井字棋规则判断是否获胜
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


# 将已经在棋盘上的棋子备份,随时更新
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)

    return dupeBoard


# 判断棋盘是否还有可落子的地方
def isSpaceFree(board, move):
    return board[move] == ' '


# 获取玩家落子的位置
def getPlayerMove(board):
    move = ' '
    # 判断落子的位置是否正确以及棋盘是否还能落子
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move?(1-9)")
        move = input()
    return int(move)


# 找到可以落子的地方，主要是计算机使用的
def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


# 电脑落子
def getComputerMove(board, computerLetter):
    # 给出棋盘上电脑和玩家棋子的类型
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        # 在备份的棋盘中判断是否有可以落子的地方
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            # 如果有可以落子的地方,则先在备份的棋盘上落子
            makeMove(copy, computerLetter, i)
            # 落子后判断电脑是否能赢,并且返回能赢的落子的位置
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            # 在备份的棋盘上模拟玩家落子
            makeMove(copy, playerLetter, i)
            # 如果下一次玩家落子就可以赢,返回玩家落子的位置,用于堵住玩家
            if isWinner(copy, playerLetter):
                return i

    # 随机在四个角处落子
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # 如果角处已被占满,则落子在中间位置5处
    if isSpaceFree(board, 5):
        return 5

    # 如果角和中间都被占满,则随机选择边上落子
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


# 判断棋盘是否已满
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("Welcome to Tictactoe !!!")

while True:

    # 初始化棋盘为空
    theBoard = [' '] * 10
    # 玩家和电脑棋子类型的选择
    playerLetter, computerLetter = inputPlayerLetter()
    # 先后顺序的决定
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first')
    # 游戏开始的标志位,当游戏结束时变成False
    gameIsPlaying = True

    while gameIsPlaying:
        # 玩家先行
        if turn == 'player':
            drawBoard(theBoard)
            # 获取玩家下棋的位置
            move = getPlayerMove(theBoard)
            # 将玩家的棋子传入列表相应的位置
            makeMove(theBoard, playerLetter, move)

            # 如果玩家获胜,标志位变为False
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("You win !")
                gameIsPlaying = False
            # 否则则判断棋盘是否已满
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Tie")
                    break
                # 若棋盘未满,且玩家已落子,则下一次落到计算机落子
                else:
                    turn = 'computer'
        # 电脑先行
        else:
            # 电脑随机选择位置落子
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            # 如果电脑落子获胜,则游戏结束
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("You lose !")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Tie")
                    break
                else:
                    turn = 'player'

    # 玩家没有再次开始游戏,则跳出循环
    if not playAgain():
        break
