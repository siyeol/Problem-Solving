from collections import deque

n = int(input())

board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))

def get_init_art(board):
    visited = [[0]*n for _ in range(n)]
    groups = list()
    groups_val = list()

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    def find_group(y, x, val):
        group = set()

        q = deque()
        q.append((y, x))
        group.add((y, x))

        while q:
            cury, curx = q.popleft()

            for i in range(4):
                yy = cury+dy[i]
                xx = curx+dx[i]

                if 0<=yy<n and 0<=xx<n and not visited[yy][xx] and board[yy][xx]==val:
                    visited[yy][xx] = 1
                    q.append((yy, xx))
                    group.add((yy, xx))

        groups.append(group)
        groups_val.append(val)

    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                visited[y][x] = 1
                find_group(y, x, board[y][x])

    # print(groups)
    # print(groups_val)

    num_groups = len(groups)

    def get_johwa(first, second):
        a_can = len(groups[first])
        b_can = len(groups[second])

        a_val = groups_val[first]
        b_val = groups_val[second]

        # a_sum = a_val*a_can #sum(groups[first])
        # b_sum = b_val*b_can #sum(groups[second])

        adj_cnt = 0
        for y, x in groups[first]:
            for i in range(4):
                yy = y+dy[i]
                xx = x+dx[i]

                if 0<=yy<n and 0<=xx<n: # and not group_visited[yy][xx]:
                    # group_visited[]
                    if (yy, xx) in groups[second]:
                        adj_cnt+=1

        return (a_can+b_can)*a_val*b_val*adj_cnt

    init_art = 0
    for first in range(num_groups-1):
        for second in range(first+1, num_groups):
            init_art+=get_johwa(first, second)
            # print(get_johwa(first, second))

    return init_art

from copy import deepcopy

dx1 = [0, -1, 0, 1]
dy1 = [-1, 0, 1, 0]

dx2 = [1, 0, -1, 0]
dy2 = [0, -1, 0, 1]

def rotate_board(board):
    rboard = [[0]*n for _ in range(n)]

    crossq = deque()
    midy, midx = n//2, n//2
    for far in range(1, n//2+1):
        for i in range(4):
            yy = midy + far*dy2[i]
            xx = midx + far*dx2[i]
            crossq.append(board[yy][xx])

    for far in range(1, n//2+1):
        for i in range(4):
            yy = midy + far*dy1[i]
            xx = midx + far*dx1[i]
            rboard[yy][xx] = crossq.popleft()

    rboard[midy][midx] = board[midy][midx]
    tempq = deque()
    #section 1
    for x in range(0, n//2):
        for y in range(n//2-1, -1, -1):
            tempq.append(board[y][x])

    for y in range(0, n//2):
        for x in range(0, n//2):
            rboard[y][x] = tempq.popleft()

    tempq.clear()
    #section 2
    for x in range(n//2+1, n):
        for y in range(n//2-1, -1, -1):
            tempq.append(board[y][x])

    for y in range(0, n//2):
        for x in range(n//2+1, n):
            rboard[y][x] = tempq.popleft()

    tempq.clear()
    # section 3
    for x in range(0, n//2):
        for y in range(n-1, n//2, -1):
            tempq.append(board[y][x])

    for y in range(n//2+1, n):
        for x in range(0, n//2):
            rboard[y][x] = tempq.popleft()

    tempq.clear()
    # section 4
    for x in range(n//2+1, n):
        for y in range(n-1, n//2, -1):
            tempq.append(board[y][x])

    for y in range(n//2+1, n):
        for x in range(n//2+1, n):
            rboard[y][x] = tempq.popleft()

    tempq.clear()

    return rboard


art1 = (get_init_art(board))

rboard = rotate_board(board)
art2 = (get_init_art(rboard))

rrboard = rotate_board(rboard)
art3 = get_init_art(rrboard)

rrrboard = rotate_board(rrboard)
art4 = get_init_art(rrrboard)

print(art1+art2+art3+art4)