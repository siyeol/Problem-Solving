N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

ylen = len(board)
xlen = len(board[0])

cumul = [[0]*(N+1) for _ in range(N+1)]

for y in range(1, ylen+1):
    for x in range(1, xlen+1):
        cumul[y][x] = cumul[y-1][x] + cumul[y][x-1] - cumul[y-1][x-1] + board[y-1][x-1]

answer = list()
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer.append(cumul[x2][y2] - cumul[x1-1][y2] - cumul[x2][y1-1] + cumul[x1-1][y1-1])

for ans in answer:
    print(ans)