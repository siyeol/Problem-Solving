N, M = map(int, input().split())

board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))


dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

tetmax = 0

def DFS(y, x, prevy, prevx, visited, cnt, tetsum):
    global tetmax

    if cnt == 4:
        tetmax = max(tetmax, tetsum)
        return

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0<=yy<N and 0<=xx<M and not visited[yy][xx]:
            if cnt == 2:
                visited[yy][xx] = 1
                DFS(y, x, y, x, visited, cnt+1, tetsum+board[yy][xx])
                visited[yy][xx] = 0
            visited[yy][xx] = 1
            DFS(yy, xx, y, x, visited, cnt+1, tetsum+board[yy][xx])
            visited[yy][xx] = 0

visited = [[0]*M for _ in range(N)]
for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        DFS(y, x, _, _, visited, 1, board[y][x])
        visited[y][x] = 0

print(tetmax)