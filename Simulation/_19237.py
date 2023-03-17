N, M, k = map(int, input().split())

shark = list()
for _ in range(N):
    shark.append(list(map(int, input().split())))

dir_list = list(map(int, input().split()))

for y in range(N):
    for x in range(N):
        if shark[y][x]!=0:
            for i in range(1, M+1):
                


smell = [[[0, 0] for _ in range(N)] for _ in range(N)] #smellcnt, whose
shark_pos = list()
shark_priori = list() #sp[shark_no][shark_pos[2]]

# for i in range(1, M+1):
#     for y in range(N):
#         for x in range(N):
#             if board[y][x]==i:
#                 shark_pos.append([y, x])
#                 smell[y][x] = [k,i-1]

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

print(shark_priori)