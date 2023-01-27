"""
Leet 200 similiar
"""
from collections import deque

result_list=list()

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))

    #BFS
    y = len(grid)
    x = len(grid[0])

    visited = [[0]*n for _ in range(m)]

    dx = [0, -1, 0, 1, 1, 1, -1, -1]
    dy = [-1, 0, 1, 0, -1, 1, 1, -1]
    #clock wise
    #grid[y][x]

    def BFS(y, x):
        q = deque()
        q.append((y, x))
        visited[y][x] = 1

        while q:
            y, x = q.popleft()
            for i in range(8):
                new_x = x+dx[i]
                new_y = y+dy[i]

                if 0<= new_x < n and 0<=new_y<m and visited[new_y][new_x]==0 and grid[new_y][new_x] == 1:
                    q.append((new_y, new_x))
                    visited[new_y][new_x]=1
    count = 0


    for y in range(m):
        for x in range(n):
            if grid[y][x] == 1 and visited[y][x] == 0:
                BFS(y, x)
                count+=1

    result_list.append(count)

for result in result_list:
    print(result)