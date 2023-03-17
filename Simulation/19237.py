N, M, k = map(int, input().split())

board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))


smell = [[[0, 0] for _ in range(N)] for _ in range(N)] #smellcnt, whose
shark_pos = list()
shark_priori = list() #sp[shark_no][shark_pos[2]]

for i in range(1, M+1):
    for y in range(N):
        for x in range(N):
            if board[y][x]==i:
                shark_pos.append([y, x])
                smell[y][x] = [k,i-1]

dir_list = list(map(int, input().split()))
for i in range(M):
    shark_pos[i].append(dir_list[i]-1)

for _ in range(M):
    temp_dir = list()
    for _ in range(4):
        td = list(map(int, input().split()))
        temp_dir.append([x-1 for x in td])
    shark_priori.append(temp_dir)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

shark_check = [1]*M

def decay_smell():
    for y in range(N):
        for x in range(N):
            if smell[y][x][0]>0:
                smell[y][x][0]-=1
            if smell[y][x][0]==0:
                smell[y][x][1] = -1

def spread_smell(shark_pos):
    for idx, (y, x, dir) in enumerate(shark_pos):
        if shark_check[idx] == 1:
            smell[y][x][0] = k
            smell[y][x][1] = idx

def compete_shark(shark_pos):
    temp_idx = list()
    for i in range(len(shark_pos)-1, 0, -1):
        y, x, dir = shark_pos[i]
        for rest_shark in shark_pos[:i]:
            if rest_shark[0] == y and rest_shark[1] == x:
                temp_idx.append(i)
                # shark_pos.pop()
                shark_check[i]=0

    return shark_pos

    good_shark = list()
    
    for i in range(len(shark_pos)):
        if i not in temp_idx:
            good_shark.append(shark_pos[i])

    return good_shark

def shark_move(shark_pos):

    spread_smell(shark_pos)

    for i in range(len(shark_pos)):
        if shark_check[i] == 0:
            continue
        y, x, dir = shark_pos[i]
        
        flag = False
        for priori in shark_priori[i][dir]:
            yy = y+dy[priori]
            xx = x+dx[priori]

            if 0<=yy<N and 0<=xx<N and smell[yy][xx][0] == 0:
                shark_pos[i] = [yy, xx, priori]
                flag = True
                break

        if flag is False:
            for priori in shark_priori[i][dir]:
                yy = y+dy[priori]
                xx = x+dx[priori]

                if 0<=yy<N and 0<=xx<N and smell[yy][xx][1] == i:
                    shark_pos[i] = [yy, xx, priori]
                    break
    decay_smell()


    shark_pos = compete_shark(shark_pos)
    

    return shark_pos

from pprint import pprint

for i in range(1001):
    if shark_check[0] == 1 and sum(shark_check)==1:
        print(i)
        exit()
    else:
        shark_pos = shark_move(shark_pos)

print(-1)
