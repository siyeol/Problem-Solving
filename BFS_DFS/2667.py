from collections import deque

N = int(input())

board = [[0]*N for _ in range(N)]
for y in range(N):
    temp = input()
    for x in range(N):
        board[y][x] = int(temp[x])

visited = [[0]*N for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# result_count = 0
result_list = list()

def BFS(y, x):
    area = 1

    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        yy, xx = q.popleft()

        for i in range(4):
            new_y = yy + dy[i]
            new_x = xx + dx[i]

            if 0<=new_y<N and 0<=new_x<N:
                if board[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                    q.append((new_y, new_x))
                    visited[new_y][new_x] = 1
                    area+=1

    return area


for y in range(N):
    for x in range(N):
        if board[y][x] == 1 and visited[y][x] == 0:
            result_list.append(BFS(y, x))

print(len(result_list))
for rl in (sorted(result_list)):
    print(rl)