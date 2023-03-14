from collections import deque
from copy import deepcopy

N, M = map(int, input().split())

board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def spread_virus (board):
    visited = [[0]*M for _ in range(N)]
    
    temp_board = deepcopy(board)
    def BFS(y, x):
        q = deque()
        q.append((y, x))
        visited[y][x] = 1
        temp_board[y][x] = 2

        while q:
            cury, curx = q.popleft()
            for i in range(4):
                yy = cury+dy[i]
                xx = curx+dx[i]

                if 0<=yy<N and 0<=xx<M and not visited[yy][xx]:
                    if temp_board[yy][xx]==0:
                        q.append((yy, xx))
                        visited[yy][xx]=1
                        temp_board[yy][xx]=2

    for y in range(N):
        for x in range(M):
            if temp_board[y][x] == 2:
                BFS(y, x)

    return temp_board


max_virus = 0

def calculate_safe(board):
    cnt = 0
    board = spread_virus(board)
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                cnt+=1

    global max_virus
    max_virus = max(max_virus, cnt)



def backtrack(num_wall):
    if num_wall == 3:
        calculate_safe(board)
        return

    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                board[y][x] = 1
                backtrack(num_wall+1)
                board[y][x] = 0

backtrack(0)

print(max_virus)