from collections import deque

N, M = map(int, input().split())

r, c, d = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False]*M for _ in range(N)]

visited[r][c]=True

q = deque()
q.append((r, c, d))

count =0
while True:
    
    isFour = False
    for i in range(4):
        d = (d+3)%4
        r_in, c_in, d_in = r, c, d
        r_in = r_in + dy[d_in] 
        c_in = c_in + dx[d_in]
        if 0<=r_in<N and 0<=c_in<M and graph[r_in][c_in] ==0 and visited[r_in][c_in] is False:
            r = r_in
            c = c_in
            count+=1
            isFour = True
            visited[r_in][c_in] = True
            break
        else:
            continue
    
    if isFour is False: 
        if graph[r-dy[d]][c-dx[d]] == 0:
            r -= dy[d]
            c -= dx[d]
            # visited[r][c] = True
        else:
            count+=1
            break

print(count)    

