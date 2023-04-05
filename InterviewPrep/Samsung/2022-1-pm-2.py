n,m,k,c = map(int, input().split())

tree_board = list()
pest_board = [[0]*n for _ in range(n)]

for _ in range(n):
    tree_board.append(list(map(int, input().split())))

dead_tree = 0

diagx = [1, 1, -1, -1]
diagy = [-1, 1, -1, 1]

adjx = [0, 1, 0, -1]
adjy = [1, 0 ,-1, 0]

from copy import deepcopy
def grow(tree_board):
    for y in range(n):
        for x in range(n):
            if tree_board[y][x] > 0:
                cnt_adj = 0
                for i in range(4):
                    yy = y+adjy[i]
                    xx = x+adjx[i]
                    if 0<=yy<n and 0<=xx<n and tree_board[yy][xx]>0:
                        cnt_adj+=1
                tree_board[y][x]+=cnt_adj
    return tree_board

def populate(tree_board):
    temp_tree = deepcopy(tree_board)
    for y in range(n):
        for x in range(n):
            if temp_tree[y][x]>0:
                cnt_possible = 0
                for i in range(4):
                    yy = y+adjy[i]
                    xx = x+adjx[i]
                    if 0<=yy<n and 0<=xx<n and temp_tree[yy][xx]==0 and pest_board[yy][xx]==0:
                        cnt_possible+=1
                if cnt_possible:
                    for i in range(4):
                        yy = y + adjy[i]
                        xx = x + adjx[i]
                        if 0 <= yy < n and 0 <= xx < n and temp_tree[yy][xx] == 0 and pest_board[yy][xx]==0:
                            tree_board[yy][xx] += (temp_tree[y][x]//cnt_possible)
    return tree_board

def kill(tree_board, pest_board):
    max_pest_sum = 0
    max_pest_loc = (0, 0)

    for y in range(n):
        for x in range(n):
            if tree_board[y][x]>0:
                cur_pest_sum = tree_board[y][x]
                for i in range(4):
                    for ki in range(1, k+1):
                        yy = y+ki*diagy[i]
                        xx = x+ki*diagx[i]
                        if 0<=yy<n and 0<=xx<n and tree_board[yy][xx]>0:
                            cur_pest_sum+=tree_board[yy][xx]
                        else:
                            break

                if cur_pest_sum>max_pest_sum:
                    max_pest_sum=cur_pest_sum
                    max_pest_loc=(y, x)


    global dead_tree
    dead_tree += max_pest_sum

    if tree_board[max_pest_loc[0]][max_pest_loc[1]] > 0:
        pest_board[max_pest_loc[0]][max_pest_loc[1]] = c
        tree_board[max_pest_loc[0]][max_pest_loc[1]] = 0
        for i in range(4):
            for ki in range(1, k+1):
                yy = max_pest_loc[0] + ki * diagy[i]
                xx = max_pest_loc[1] + ki * diagx[i]
                if 0 <= yy < n and 0 <= xx < n and tree_board[yy][xx] > 0:
                    pest_board[yy][xx] = (c)
                    tree_board[yy][xx] = 0
                elif 0<=yy<n and 0<=xx<n and tree_board[yy][xx] == 0:
                    pest_board[yy][xx] = (c)
                    break
                else:
                    break

    return tree_board, pest_board

def pest_decay(pest_board):
    for y in range(n):
        for x in range(n):
            if pest_board[y][x] > 0:
                pest_board[y][x]-=1
    return pest_board

from pprint import pprint

for _ in range(m):
    tree_board = grow(tree_board)
    # pprint(tree_board)

    tree_board = populate(tree_board)
    # pprint(tree_board)

    # pprint(pest_board)
    pest_board = pest_decay(pest_board)

    tree_board, pest_board = kill(tree_board, pest_board)

    # pprint(tree_board)
    # pprint(pest_board)

print(dead_tree)
