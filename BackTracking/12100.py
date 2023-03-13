from collections import deque
from copy import deepcopy

N = int(input())
board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))

def up(board):
    for x in range(N):
        q = deque()        
        for y in range(N):
            #isAdded
            if board[y][x] != 0:
                if q and q[-1][1] is False and q[-1][0] == board[y][x]:
                    q.pop()
                    q.append((board[y][x]*2, True))
                else:
                    q.append((board[y][x], False))
        for y in range(N):
            if q:
                board[y][x] = q.popleft()[0]
            else:
                board[y][x] = 0
    return board

def down(board):
    for x in range(N):
        q = deque()        
        for y in range(N-1, -1, -1):
            #isAdded
            if board[y][x] != 0:
                if q and q[-1][1] is False and q[-1][0] == board[y][x]:
                    q.pop()
                    q.append((board[y][x]*2, True))
                else:
                    q.append((board[y][x], False))
        for y in range(N-1, -1, -1):
            if q:
                board[y][x] = q.popleft()[0]
            else:
                board[y][x] = 0
    return board

def left(board):
    for y in range(N):
        q = deque()        
        for x in range(N):
            #isAdded
            if board[y][x] != 0:
                if q and q[-1][1] is False and q[-1][0] == board[y][x]:
                    q.pop()
                    q.append((board[y][x]*2, True))
                else:
                    q.append((board[y][x], False))
        for x in range(N):
            if q:
                board[y][x] = q.popleft()[0]
            else:
                board[y][x] = 0
    return board

def right(board):
    for y in range(N):
        q = deque()        
        for x in range(N-1, -1, -1):
            #isAdded
            if board[y][x] != 0:
                if q and q[-1][1] is False and q[-1][0] == board[y][x]:
                    q.pop()
                    q.append((board[y][x]*2, True))
                else:
                    q.append((board[y][x], False))
        # print(q)
        for x in range(N-1, -1, -1):
            if q:
                board[y][x] = q.popleft()[0]
            else:
                board[y][x] = 0
    return board


max_block = list()

def backtrack(board, cnt):
    bm = 0
    for b in board:
        bm = max(bm, max(b))

    max_block.append(bm)

    if cnt == 5:
        return

    backtrack(up(deepcopy(board)), cnt+1)
    backtrack(down(deepcopy(board)), cnt+1)
    backtrack(left(deepcopy(board)), cnt+1)
    backtrack(right(deepcopy(board)), cnt+1)
    
backtrack(board, 0)

print(max(max_block))