from collections import deque

n, m = map(int, input().split())

board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]

user_pos = deque()
user_dest = deque()
user_visited = deque()

user_input = deque()
for _ in range(m):
    y, x = map(int, input().split())
    user_input.append([y-1, x-1])

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def find_basecamp(y, x): #start = 편의점
    check = [[0] * n for _ in range(n)]
    route = ""
    q = deque()
    q.append((y, x, 0))
    check[y][x] = 1

    basecamp_list = list()

    while q:
        cury, curx, curdist = q.popleft()

        if board[cury][curx] == 1:
            basecamp_list.append((cury, curx, curdist))

        for i in range(4):
            yy = cury+dy[i]
            xx = curx+dx[i]

            if 0<=yy<n and 0<=xx<n and not check[yy][xx] and not visited[yy][xx]:
                check[yy][xx] = 1
                q.append((yy, xx, curdist+1))

    basecamp_list.sort(key = lambda x: x[1])
    basecamp_list.sort(key = lambda x: x[0])
    basecamp_list.sort(key = lambda x: x[2])

    board[basecamp_list[0][0]][basecamp_list[0][1]] = 0
    return basecamp_list[0][0], basecamp_list[0][1]


def find_next (starty, startx, desty, destx):
    check = [[0]*n for _ in range(n)]
    q = deque()
    route = ""
    q.append((starty, startx, route))
    check[starty][startx]=1

    while q:
        cury, curx, curroute = q.popleft()

        if cury == desty and curx == destx:
            return curroute

        for i in range(4):
            yy = cury+dy[i]
            xx = curx+dx[i]

            if 0<=yy<n and 0<=xx<n and not check[yy][xx] and not visited[yy][xx]:
                check[yy][xx] = 1
                q.append((yy, xx, curroute+str(i)))


def play():
    # 1 MOVE
    for up in range(len(user_pos)):
        route = find_next(user_pos[up][0],user_pos[up][1], user_dest[up][0], user_dest[up][1])
        # print(user_pos[up], int(route[0]))
        user_pos[up][0] += dy[int(route[0])]
        user_pos[up][1] += dx[int(route[0])]

    # 2
    for up in range(len(user_pos)-1, -1, -1):
        if user_pos[up] == user_dest[up]:
            visited[user_pos[up][0]][user_pos[up][1]] = 1
            del user_pos[up]
            del user_dest[up]

    # 3
    if user_input:
        new_user = user_input.popleft()
        user_dest.append(new_user)

        start_y, start_x = find_basecamp(new_user[0], new_user[1])
        user_pos.append([start_y, start_x])

        visited[start_y][start_x] = 1

cnt = 0
while True:
    play()
    cnt+=1
    if len(user_pos) == 0:
        break

print(cnt)