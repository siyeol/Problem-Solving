from math import inf
from copy import deepcopy

min_cnt = inf

N, M = map(int, input().split())

board = list()
cctv_list = list()

for y in range(N):
    temp_list = list(map(int, input().split()))
    for x in range(M):
        if temp_list[x] in range(1, 6):
            cctv = 'c'+str(temp_list[x])
            cctv_list.append((y, x, cctv))
    board.append(temp_list)

cctv_dict = dict()
cctv_dict['c1'] = [[[0, 1]], [[0, -1]], [[1, 0]], [[-1, 0]]]
cctv_dict['c2'] = [[[1, 0], [-1, 0]],[[0, 1], [0, -1]]]
cctv_dict['c3'] = [[[1, 0], [0, 1]],[[1, 0], [0, -1]],[[-1, 0], [0, 1]],[[-1, 0], [0, -1]]]
cctv_dict['c4'] = [[[1, 0], [-1, 0], [0, -1]], [[0, 1], [-1, 0], [0, -1]], [[0, 1], [1, 0], [0, -1]], [[0, 1], [1, 0], [-1, 0]]]
cctv_dict['c5'] = [[[0, 1], [1, 0], [-1, 0], [0, -1]]]

visited = [[0]*M for _ in range(N)]

def color(board, y, x, dir_list):
    for dir in dir_list:
        tempy, tempx = y, x
        while True:
            tempy+=dir[0]
            tempx+=dir[1]
            if 0<=tempy<N and 0<=tempx<M:
                if board[tempy][tempx] == 0:
                    board[tempy][tempx] = -1
                if board[tempy][tempx] == 6:
                    break
            else:
                break
    return board

def cnt_sagak(board):
    cnt_total = 0
    for bd in board:
        cnt_total+=bd.count(0)
    return cnt_total

def DFS(cctv_list_idx, lab_board):
    if cctv_list_idx == len(cctv_list):
        global min_cnt
        min_cnt = min(min_cnt, cnt_sagak(lab_board))
        return

    for dl in cctv_dict[cctv_list[cctv_list_idx][-1]]:
        DFS(cctv_list_idx+1, color(deepcopy(lab_board), cctv_list[cctv_list_idx][0], cctv_list[cctv_list_idx][1], dl))

DFS(0, board)

print(min_cnt)