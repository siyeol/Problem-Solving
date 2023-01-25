import sys
sys.setrecursionlimit(2500)

N = int(input())

og_board = [[0]*N for _ in range(N)]

def color_movable(board, i, j):
    for n in range(N):
        board[n][j]=1
        board[i][n]=1

        iplus = i+n
        jplus = j+n
        iminus = i-n
        jminus = j-n

        if 0<=jplus<N and 0<=iplus<N:
            board[iplus][jplus]=1
        if 0<=jplus<N and 0<=iminus<N:
            board[iminus][jplus]=1
        if 0<=jminus<N and 0<=iplus<N:
            board[iplus][jminus]=1
        if 0<=jminus<N and 0<=iminus<N:
            board[iminus][jminus]=1
    
    return board

from pprint import pprint
from copy import deepcopy
case = 0

def Nqueen(board, ii, count):
    global case
    for i in range(ii, N):
        if sum(board[i])==N:
            continue
        for j in range(N):
            if board[i][j]==0:
                temp_board = deepcopy(board)
                if count == N-1:
                    case+=1
                    # pprint(board)
                    return
                Nqueen(color_movable(temp_board, i, j), i+1, count+1)
                # break

Nqueen(og_board, 0, 0)

print(case)