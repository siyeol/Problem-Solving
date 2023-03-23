from math import inf

N, M, H = map(int, input().split())

connect = [[0] * (N-1) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    connect[a-1][b-1] = 1

def play():
    for player in range(N):
        init_player = player
        
        for i in range(H):
            if player == 0:
                if connect[i][player]:
                    player+=1
            elif player == N-1:
                if connect[i][-1]:
                    player-=1
            else:
                if connect[i][player]:
                    player+=1
                else:
                    if connect[i][player-1]:
                        player-=1
        
        if player!=init_player:
            return False

    return True


ans_cnt = inf

glb_cnt = 0

searched = list()
def DFS(add_cnt, new_y, new_x):
    if add_cnt > 3:
        # ans_cnt = -1
        return

    if play():
        global ans_cnt
        ans_cnt = min(ans_cnt, add_cnt)
        return
    
    for y in range(new_y, H):
        new_x = new_x if y == new_y else 0
        for x in range(new_x, N-1):
            if connect[y][x] == 0:
                connect[y][x] = 2
                DFS(add_cnt+1, y, x+1)
                connect[y][x] = 0

DFS(0, 0, 0)
# print(glb_cnt)
if ans_cnt == inf:
    print(-1)
else:
    print(ans_cnt)