from collections import deque

# import sys 
# sys.setrecursionlimit(10**6)

N = int(input())

human = [[""] * N for _ in range(N)]
cow = [[""] * N for _ in range(N)] #only with Green and Blue

for y in range(N):
    row = input()
    for x in range(N):
        human[y][x] = row[x]
        if row[x] == "R": 
            cow[y][x] = "G"
        else:
            cow[y][x] = row[x]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


#BFS Solution

def BFS(board,visited, y, x):

    visited[y][x]=1
    q = deque()
    q.append((y, x))

    while q:
        cury, curx = q.popleft()
        for i in range(4):
            newy = cury + dy[i]
            newx = curx + dx[i]

            if 0<=newy<N and 0<=newx<N:
                if not visited[newy][newx] and board[cury][curx] == board[newy][newx]:
                    q.append((newy, newx))
                    visited[newy][newx] = 1


def get_value(board):
    visited = [[0] * N for _ in range(N)]

    count = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                BFS(board,visited, y, x)
                count += 1

    return count

human_cnt = get_value(human)
cow_cnt = get_value(cow)

print(human_cnt, cow_cnt)


'''
DFS solution
visited = [[0] * N for _ in range(N)]

def DFS_human(board, y, x):
    visited[y][x] = 1

    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]

        if 0<=newy<N and 0<=newx<N:
            if not visited[newy][newx] and board[y][x] == board[newy][newx]:
                visited[newy][newx]
                DFS_human(board, newy, newx)

count = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            DFS_human(human, y, x)
            count += 1

visited = [[0] * N for _ in range(N)]
count2 = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            DFS_human(cow, y, x)
            count2 += 1

print(count, count2)

'''
