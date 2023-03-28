from copy import deepcopy
from collections import deque
R, C, T = map(int, input().split())

board = list()
for _ in range(R):
    board.append(deque(map(int, input().split())))

for y in range(R):
    if board[y][0] == -1:
        airp1 = (y, 0)
        airp2 = (y+1, 0)
        break

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def spread(board):
    spread_board = deepcopy(board)
    for y in range(R):
        for x in range(C):
            if board[y][x] > 0:
                spread_cnt = 0
                for i in range(4):
                    yy = y+dy[i]
                    xx = x+dx[i]
                    if 0<=yy<R and 0<=xx<C and board[yy][xx]!=-1:
                        spread_cnt+=1
                        spread_board[yy][xx] += board[y][x]//5
                spread_board[y][x] -= (spread_cnt*(board[y][x]//5))
                # pprint(spread_board)
    return spread_board

def purify(board):
    # move down
    for y in range(airp1[0] - 2, -1, -1):
        board[y + 1][0] = board[y][0]

    left_end = board[0].popleft()
    board[0].append(0)

    # move up
    for y in range(airp1[0]):
        board[y][C - 1] = board[y + 1][C - 1]

    right_end = board[airp1[0]].pop()
    board[airp1[0]].insert(1, 0)

    #P2
    # move up
    for y in range(airp2[0]+1, R-1):
        board[y][0] = board[y + 1][0]

    left_end = board[-1].popleft()
    board[-1].append(0)

    # move down
    for y in range(R-2, airp2[0]-1, -1):
        board[y + 1][C-1] = board[y][C-1]

    right_end = board[airp2[0]].pop()
    board[airp2[0]].insert(1, 0)

    return board

for _ in range(T):
    board = purify(spread((board)))

total = 0
for row in board:
    total+=sum(row)
# board = spread(board)
print(total+2)
# print(purify(board))