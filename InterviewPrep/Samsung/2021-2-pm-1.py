from collections import deque
from pprint import pprint

monster_board = [[deque() for _ in range(4)] for _ in range(4)]
dead_board = [[deque() for _ in range(4)] for _ in range(4)]
egg_board = [[deque() for _ in range(4)] for _ in range(4)]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

m, t = map(int, input().split())
r, c = map(int, input().split())
pacy, pacx = r-1, c-1

for i in range(m):
    rr, cc, dd = map(int, input().split())
    monster_board[rr-1][cc-1].append(dd-1)

#1. monster dup
def dup_monster():
    for y in range(4):
        for x in range(4):
            if monster_board[y][x]:
                for monster in monster_board[y][x]:
                    egg_board[y][x].append(monster)

#알 여러개 가능?

#2 monster move
from copy import deepcopy
def monster_move():
    temp_board = deepcopy(monster_board)
    for y in range(4):
        for x in range(4):
            if temp_board[y][x]:
                for idx in range(len(temp_board[y][x])):
                    flag = False
                    for i in range(8):
                        di = (temp_board[y][x][idx] + i) % 8
                        yy = y+dy[di]
                        xx = x+dx[di]
                        if 0<=yy<4 and 0<=xx<4 and (pacx!=xx or pacy!=yy) and not dead_board[yy][xx]:
                            monster_board[y][x].popleft()
                            monster_board[yy][xx].append(di)
                            flag = True
                            break
                    if flag is False:
                        monster_board[y][x].append(monster_board[y][x].popleft())

#3 pacman move

pdy = [-1, 0, 1, 0]
pdx = [0, -1, 0, 1]
#DFS with depth 3
dfs_result = list()
dfs_visited = [[0]*4 for _ in range(4)]
def DFS(y, x, cnt, depth, route):
    if depth == 3:
        dfs_result.append([cnt, route])
        return

    for i in range(4):
        yy = y+pdy[i]
        xx = x+pdx[i]

        if 0<=yy<4 and 0<=xx<4 and not dfs_visited[yy][xx]:
            dfs_visited[yy][xx] = 1
            if monster_board[yy][xx]:
                DFS(yy, xx, cnt+len(monster_board[yy][xx]), depth+1, route+str(i))
            else:
                DFS(yy, xx, cnt, depth + 1, route + str(i))
            dfs_visited[yy][xx] = 0

def eat_pac(route):
    global pacy, pacx

    for cmd in route:
        di = int(cmd)
        pacy += pdy[di]
        pacx += pdx[di]

        if monster_board[pacy][pacx]:
            while monster_board[pacy][pacx]:
                monster_board[pacy][pacx].pop()
                dead_board[pacy][pacx].append(2)

#4 monster deacy
def dead_decay():
    for y in range(4):
        for x in range(4):
            if dead_board[y][x]:
                for idx in range(len(dead_board[y][x])-1, -1, -1):
                    if dead_board[y][x][idx]>0:
                        dead_board[y][x][idx]-=1
                    else:
                        del dead_board[y][x][idx]
#5 monster dup finish
def wake_egg():
    for y in range(4):
        for x in range(4):
            if egg_board[y][x]:
                while egg_board[y][x]:
                    monster_board[y][x].append(egg_board[y][x].pop())

def play():
    dup_monster()
    monster_move()

    dfs_visited[pacy][pacx] = 1
    DFS(pacy, pacx, 0, 0, "")
    dfs_result.sort(key= lambda x:x[1])
    dfs_result.sort(key= lambda x:x[0], reverse=True)
    # print(dfs_result)
    eat_route = dfs_result[0][1]
    eat_pac(eat_route)

    dfs_result.clear()
    for y in range(4):
        for x in range(4):
            dfs_visited[y][x]=0

    dead_decay()
    wake_egg()

def get_monster():
    cnt = 0
    for y in range(4):
        for x in range(4):
            cnt+=len(monster_board[y][x])
    return cnt



pprint(monster_board)
pprint(dead_board)
pprint(egg_board)
print(pacy, pacx)

for _ in range(t):
    play()

    pprint(monster_board)
    pprint(dead_board)
    pprint(egg_board)
    print(pacy, pacx)

print(get_monster())
