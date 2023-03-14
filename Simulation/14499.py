N, M, y, x, K = map(int, input().split())

dice = [0, 0, 0, 0, 0, 0, 0]
# 동, 서, 남, 북, 상, 하

# 3, 4, 2, 5, 1, 6

# 1, 6, 2, 5, 4, 3
# 6, 1, 2, 5, 3, 4
# 3, 4, 6, 1, 2, 5
# 3, 4, 1, 6, 5, 2

# 동 서 북 남

def roll_dice (dir):
    global dice
    if dir == 1:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[6], dice[2], dice[1]
    elif dir == 2:
        dice[1], dice[2], dice[5], dice[6] = dice[6], dice[5], dice[1], dice[2]
    elif dir == 3:
        dice[3], dice[4], dice[5], dice[6] = dice[6], dice[5], dice[3], dice[4]
    else:
        dice[3], dice[4], dice[5], dice[6] = dice[5], dice[6], dice[4], dice[3]

board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))
    
command = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


for cmd in command:
    cmd -= 1
    
    new_y = y+dy[cmd]
    new_x = x+dx[cmd]
    
    if 0<=new_y<N and 0<=new_x<M:
        y = new_y
        x = new_x
        roll_dice(cmd+1)

        if board[y][x] == 0:
            board[y][x] = dice[-1]
        else:
            dice[-1] = board[y][x]
            board[y][x] = 0

        print(dice[-2])
    else:
        pass
