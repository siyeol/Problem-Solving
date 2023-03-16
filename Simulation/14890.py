N, L = map(int, input().split())
board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))
    
def check_line(line):
    for i in range(1, N):
        if line[i]-line[i-1]==1:
            for j in range(L):
                if i-j-1 < 0 or line[i-1]!=line[i-j-1] or visited[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    visited[i-j-1] = 1
        elif line[i-1]-line[i] == 1:
            for j in range(L):
                if i+j>=N or line[i]!=line[i+j] or visited[i+j]:
                    return False
                if line[i] == line[i+j]:
                    visited[i+j] = 1    
        elif line[i] == line[i-1]:
            continue
        else:
            return False
    return True

result = 0
for row in board:
    visited = [0]*N
    if (check_line(row)):
        result+=1
    
for x in range(N):
    visited = [0]*N
    col = list()
    for y in range(N):
        col.append(board[y][x])
    if (check_line(col)):
        result+=1

print(result)
