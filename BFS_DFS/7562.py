from collections import deque

n = int(input())

dy = [-1, -2, -2, -1, 1, 2, 1 ,2]
dx = [-2, -1, 1, 2, -2, -1, 2 ,1]


def BFS(y, x, desty, destx, I):
    q = deque()
    q.append((y, x))

    while q:
        yy, xx = q.popleft()

        if yy == desty and xx == destx:
            return visited[yy][xx]
            
        for i in range(8):
            newy = yy + dy[i]
            newx = xx + dx[i]

            if 0<=newy<I and 0<=newx<I:
                if not visited[newy][newx]:
                    q.append((newy, newx))
                    visited[newy][newx] = visited[yy][xx]+1


result_list = list()
for _ in range(n):
    I = int(input())
    starty, startx = map(int, input().split())
    endy, endx = map(int, input().split())

    visited = [[0]*I for _ in range(I)]

    result_list.append(BFS(starty, startx, endy, endx, I))

for rl in result_list:
    print(rl)