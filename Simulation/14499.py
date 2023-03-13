N, M, x, y, K = map(int, input().split())

board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))
    
command = list(map(int, input().split()))

print(board, command)