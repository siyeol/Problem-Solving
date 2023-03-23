from collections import deque
from copy import deepcopy
from math import inf
from pydoc import visiblename
N, M = map(int, input().split())

board = list()
chicken = list()
houses = list()
for y in range(N):
    temp_list = list(map(int, input().split()))
    for x in range(len(temp_list)):
        if temp_list[x] == 2:
            chicken.append((y, x))
        if temp_list[x] == 1:
            houses.append((y, x))
    board.append(temp_list)

visited = [[0]*N for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def BFS(y, x):
    q = deque()
    visited[y][x] = 1
    q.append((y, x))

    while q:
        cury, curx = q.popleft()

        if board[cury][curx] == 2:
            break

        for i in range(4):
            yy = cury+dy[i]
            xx = curx+dx[i]

            if 0<=yy<N and 0<=xx<N and not visited[yy][xx]:
                # if board[yy][xx] == 
                visited[yy][xx] = 1
                q.append((yy, xx))

for house in houses:
    BFS(house[0], house[1])
