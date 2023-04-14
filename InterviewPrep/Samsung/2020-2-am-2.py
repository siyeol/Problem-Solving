from collections import deque

def solve():
    n, m, k = map(int, input().split())

    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    board = [[deque() for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        y, x, m, s, d = map(int, input().split())
        board[y-1][x-1].append((m, s, d))

    def move(board):
        add_board = [[deque() for _ in range(n)] for _ in range(n)]
        for y in range(n):
            for x in range(n):
                if board[y][x]:
                    while board[y][x]:
                        mm, ms, md = board[y][x].popleft()

                        yy = (y+ms*dy[md])%n
                        xx = (x+ms*dx[md])%n

                        add_board[yy][xx].append((mm, ms, md))
        return add_board

    straight=[0, 2, 4, 6]
    diag= [1, 3, 5, 7]

    def converge(board):
        add_board = [[deque() for _ in range(n)] for _ in range(n)]
        for y in range(n):
            for x in range(n):
                if len(board[y][x])>=2:
                    sum_m, sum_s, even_d = 0, 0, 0
                    cnt = 0
                    while board[y][x]:
                        mm, ms, md = board[y][x].popleft()
                        sum_m+=mm
                        sum_s+=ms
                        cnt += 1
                        if md %2 == 0:
                            even_d+=1
                    new_m=sum_m//5
                    new_s=sum_s//cnt
                    if even_d == cnt or even_d==0:
                        new_d = 0 #straight
                    else:
                        new_d = 1 #diag

                    if new_m > 0:
                        for i in range(4):
                            if new_d == 0:
                                add_board[y][x].append((new_m, new_s, straight[i]))
                            else:
                                add_board[y][x].append((new_m, new_s, diag[i]))

        for y in range(n):
            for x in range(n):
                if add_board[y][x]:
                    while add_board[y][x]:
                        board[y][x].append(add_board[y][x].popleft())
        return board

    def get_mass(board):
        total = 0
        for y in range(n):
            for x in range(n):
                length = len(board[y][x])
                if length:
                    temp_sum = 0
                    while board[y][x]:
                        m, _, _ = board[y][x].popleft()
                        temp_sum+=m
                    if temp_sum//length>0:
                        total+=temp_sum
        return total

    for _ in range(k):
        board = move(board)
        board = converge(board)


    return get_mass(board)

it = int(input())

for i in range(1, it+1):
    answer = solve()
    print("#%d %d"%(i, answer))

'''
2
4 4 1
1 2 2 2 4
2 4 5 3 6
4 2 1 1 0
4 3 3 2 5
4 4 2
1 2 2 2 4
2 4 5 3 6
4 2 1 1 0
4 3 3 2 5
'''