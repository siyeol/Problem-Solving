from copy import deepcopy
board = [[] for _ in range(4)]

for i in range(4):
    temp_list = list(map(int, input().split()))
    for idx, temp in enumerate(temp_list):
        if idx%2==0:
            board[i].append([temp_list[idx], temp_list[idx+1]-1])

sx = 0
sy = 0
sd = board[sy][sx][1]

yy = [-1, -1, 0, 1, 1, 1, 0, -1]
xx = [0, -1, -1, -1, 0, 1, 1, 1]

def individual_fish (i, j, d, board, sx, sy):
    for turn in range(8):
        dd = (d+turn)%8
        ii = i+yy[dd]
        jj = j+xx[dd]
        if 0<=ii<4 and 0<=jj<4 and (ii!=sy or jj!=sx):
            board[i][j][1] = dd
            board[i][j], board[ii][jj] = board[ii][jj], board[i][j]
            break
    return board

def find_position(board, fishno):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == fishno:
                return i, j
    return None, None

def move_fish (board, sx, sy):
    for fishno in range(1, 17):
        i, j = find_position(board, fishno)
        if i is not None and j is not None:
            board = individual_fish(i, j, board[i][j][1], board, sx, sy)
    return board


result = 0

def DFS(sx, sy, seat, board):
    global result
    board = deepcopy(board)
    seat += board[sy][sx][0]
    
    board[sy][sx][0] = -1
    board = move_fish(board, sx, sy)
    sxx, syy = sx, sy
    sd = board[syy][sxx][1]

    shark_candid = list()
    for _ in range(3):
        sxx += xx[sd]
        syy += yy[sd]
        if 0<= syy < 4 and 0<=sxx<4 and board[syy][sxx][0] != -1:
            shark_candid.append([sxx, syy])
    
    if shark_candid:
        for sx_in, sy_in in shark_candid:
            DFS(sx_in, sy_in, seat, board)
    else:
        result = max(result, seat)
        return

DFS(0, 0, 0, board)

print(result)