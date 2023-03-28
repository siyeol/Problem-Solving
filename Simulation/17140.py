r, c, k = map(int, input().split())

board = [[0]*100 for _ in range(100)]
for y in range(3):
    for idx, x in enumerate(map(int, input().split())):
        board[y][idx] = x


def R_cal(board):
    Yb, Xb = 0, 0
    for y in range(100):
        new_row = dict()
        for x in range(100):
            if board[y][x] == 0:
                continue
            if board[y][x] not in new_row:
                new_row[board[y][x]] = 1
            else:
                new_row[board[y][x]]+=1
        nri = new_row.items()
        nris = sorted(nri, key = lambda x :x[0])
        nris = sorted(nris, key = lambda x :x[1])
        # print(nris)

        pad_idx = 0
        for x in range(len(nris)):
            if 2*x+1 <= 99:
                board[y][2*x] = nris[x][0]
                board[y][2*x+1] = nris[x][1]
                pad_idx = 2*x+1

        Xb = max(Xb, pad_idx+1)
        for pi in range(pad_idx+1, 100):
            board[y][pi] = 0

        if len(nri)>=1 and Yb<=99:
            Yb+=1
        # Yb = max(Yb, len(nri))
    return board, Yb, Xb


def C_cal(board):
    Yb, Xb = 0, 0
    for x in range(100):
        new_row = dict()
        for y in range(100):
            if board[y][x] == 0:
                continue
            if board[y][x] not in new_row:
                new_row[board[y][x]] = 1
            else:
                new_row[board[y][x]]+=1
        nri = new_row.items()
        nris = sorted(nri, key = lambda x :x[0])
        nris = sorted(nris, key = lambda x :x[1])

        pad_idx = 0
        for y in range(len(nris)):
            if 2*y+1 <= 99:
                board[2*y][x] = nris[y][0]
                board[2*y+1][x] = nris[y][1]
                pad_idx = 2*y+1

        Yb = max(Yb, pad_idx + 1)
        for pi in range(pad_idx+1, 100):
            board[pi][x] = 0

        if len(nri)>=1 and Xb<=99:
            Xb+=1
        # Xb = max(Xb, len(nri))
    return board, Yb, Xb


Yb, Xb = 3, 3
for itercnt in range(101): #74% 에러
    if board[r-1][c-1] == k:
        print(itercnt)
        exit()
    if Yb >= Xb:
        board, Yb, Xb = R_cal(board)
    else:
        board, Yb, Xb = C_cal(board)

    #DEBUG
    # for y in range(10):
    #     for x in range(10):
    #         print(board[y][x], end=" ")
    #     print("")
print(-1)
exit()
