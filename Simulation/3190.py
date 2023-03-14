from collections import deque
from itertools import count

N = int(input())
K = int(input())

snake = deque() #(r, c)
snake.append((0, 0))
idx = 0 #direction

board = [[0]*N for _ in range(N)]
for _ in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

y, x = 0, 0
round = 0
L = int(input())

turn = dict()
for _ in range(L):
    cnt, dir = input().split()
    turn[int(cnt)] = dir

while True:
    y = y + dy[idx]
    x = x + dx[idx]

    round += 1 #time increase
    #END
    if 0<=y<N and 0<=x<N and (y, x) not in snake:
        snake.append((y, x))
        if board[y][x] == 0:
            snake.popleft()
        else:
            board[y][x] = 0
    else:
        print(round)
        break

    if round in turn:
        if turn[round] == 'D':
            idx = (idx + 1) % 4
        elif turn[round] == 'L':
            idx = (idx + 3) % 4
