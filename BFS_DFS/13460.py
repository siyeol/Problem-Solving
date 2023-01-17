from collections import deque
N, M = map(int, input().split())

board = [[None]*M for _ in range(N)]
Rx, Ry = 0, 0
Bx, By = 0, 0
Hx, Hy = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    input_str = input()
    for j in range(M):
        board[i][j] = input_str[j]
        if input_str[j] == 'R':
            Ry = i
            Rx = j
        elif input_str[j] == 'B':
            By = i
            Bx = j

visited[Ry][Rx][By][Bx]=True

q = deque()
q. append((Rx, Ry, Bx, By, 1))
# visited = list()
# visited.append((Rx, Ry, Bx, By))

result = -1
def move():
    visited = list()
    visited.append([Rx, Ry, Bx, By])
    while q:
        # print(board)
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            rxx, ryy = rx, ry
            bxx, byy = bx, by
            rcount = 0
            bcount = 0
            
            while board[byy+dy[i]][bxx+dx[i]] != '#' and board[byy][bxx] != 'O':
                bxx+=dx[i]
                byy+=dy[i]
                bcount+=1
            
            if board[byy][bxx] == 'O':
                continue

            while board[ryy+dy[i]][rxx+dx[i]] != '#' and board[ryy][rxx] != 'O':
                rxx+=dx[i]
                ryy+=dy[i]
                rcount+=1

            if board[ryy][rxx] == 'O':
                return depth
                
            if rxx == bxx and ryy == byy : # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if rcount > bcount: # 이동 거리가 많은 구슬을 한칸 뒤로
                    rxx -= dx[i]
                    ryy -= dy[i]
                else:
                    bxx -= dx[i]
                    byy -= dy[i]

            if [rxx, ryy, bxx, byy] not in visited:
                q.append((rxx, ryy, bxx, byy, depth+1))
                visited.append([rxx, ryy, bxx, byy])
    return -1
result = move()

print(result)

"""
5 5
#####
#..B#
#.#.#
#RO.#
#####
"""


"""
cur = head
prev = None
while cur:
    next = 
"""